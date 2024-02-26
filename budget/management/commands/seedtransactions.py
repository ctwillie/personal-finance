import os
import hashlib

from django.db import IntegrityError
from django.core.management.base import BaseCommand

import plaid
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest

from budget.models import Account, Category, Item, Transaction


class Command(BaseCommand):
    help = "Seeds the database with transactions"

    accounts_map = {}

    def success_message(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def warning_message(self, message):
        self.stdout.write(self.style.WARNING(message))

    def error_message(self, message):
        self.stdout.write(self.style.ERROR(message))

    def generate_unique_hash(self, input_string):
        """
        Generate a unique hash for the given string
        """
        hash_object = hashlib.sha256(input_string.encode())
        unique_hash = hash_object.hexdigest()
        return unique_hash

    def find_transaction_account(self, plaid_account_id):
        """
        Find the account with the given plaid_account_id
        """
        if plaid_account_id in self.accounts_map:
            return self.accounts_map[plaid_account_id]

        account = Account.objects.filter(plaid_account_id=plaid_account_id).first()
        if account is None:
            return None

        self.accounts_map[plaid_account_id] = account
        return account

    def handle(self, *args, **options):
        # If the transactions table is not empty, return
        if Transaction.objects.exists():
            self.warning_message("Transactions table is not empty.")
            self.warning_message(
                "Run `python manage.py updatetransactions` to update transactions."
            )
            return

        PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
        PLAID_SECRET = os.getenv("PLAID_SECRET")
        PLAID_ACCESS_TOKEN = os.getenv("PLAID_ACCESS_TOKEN")

        configuration = plaid.Configuration(
            host=plaid.Environment.Development,
            api_key={
                "clientId": PLAID_CLIENT_ID,
                "secret": PLAID_SECRET,
            },
        )
        api_client = plaid.ApiClient(configuration)
        plaid_client = plaid_api.PlaidApi(api_client)
        transactions = []
        uncategorized_transactions = []

        # Retrieve all categories mapped with keys of detailed_name and values of id
        categories = Category.objects.all()
        category_map = {category.detailed_name: category.id for category in categories}

        def fetch_transactions_historical(plaid_access_token, next_cursor=""):
            """
            Retrieve Transactions History
            """
            request = TransactionsSyncRequest(
                access_token=plaid_access_token,
                cursor=next_cursor,
            )
            return plaid_client.transactions_sync(request).to_dict()

        # For each item in the database, fetch the transactions history
        for item in Item.objects.all():
            response = fetch_transactions_historical(PLAID_ACCESS_TOKEN)
            has_more = response["has_more"]
            next_cursor = response["next_cursor"]
            transactions.extend(response["added"])

            while has_more:
                response = fetch_transactions_historical(
                    PLAID_ACCESS_TOKEN, next_cursor
                )
                transactions.extend(response["added"])
                has_more = response["has_more"]
                next_cursor = response["next_cursor"]

            for transaction in transactions:
                account = self.find_transaction_account(transaction["account_id"])
                category = category_map.get(
                    transaction["personal_finance_category"]["detailed"]
                )

                if account is None:
                    self.warning_message(
                        "Unable to find account with plaid_account_id {transaction['account_id']}"
                    )
                    continue

                if category is None:
                    uncategorized_transactions.append(transaction)
                    continue

                try:
                    Transaction.objects.create(
                        account=account,
                        hash=self.generate_unique_hash(transaction["transaction_id"]),
                        plaid_transaction_id=transaction["transaction_id"],
                        category_id=category,
                        description=transaction["name"],
                        amount=transaction["amount"],
                        date=transaction["date"],
                    )
                except Exception as e:
                    if type(e) == IntegrityError:
                        self.warning_message(
                            f"Transaction {transaction['transaction_id']} already exists in the database"
                        )
                    else:
                        self.warning_message(
                            f"Unable to add transaction {transaction['transaction_id']} to the database: {e}"
                        )

            # Clear the accounts_map for the next item
            self.accounts_map = {}

            self.success_message(
                f"Added {len(transactions) - len(uncategorized_transactions)} transactions to the database"
            )

            if len(uncategorized_transactions) > 0:
                self.warning_message(
                    f"Unable to categorize {len(uncategorized_transactions)} transactions"
                )
