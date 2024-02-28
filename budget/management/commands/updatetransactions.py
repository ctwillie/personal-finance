import os
import hashlib

from django.core.management.base import BaseCommand

import plaid
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest

from budget.models import Account, Category, Item, Transaction


class Command(BaseCommand):
    help = "Update the transactions table with the latest transactions from Plaid."

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

    def handle_added_and_modified_transactions(self, added, category_map):
        """
        Upsert the added and modified transactions in the database
        """
        uncategorized_transactions = []

        for transaction in added:
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
                Transaction.objects.update_or_create(
                    hash=self.generate_unique_hash(transaction["transaction_id"]),
                    defaults={
                        "account": account,
                        "plaid_transaction_id": transaction["transaction_id"],
                        "category_id": category,
                        "description": transaction["name"],
                        "amount": transaction["amount"],
                        "date": transaction["date"],
                    },
                )
            except Exception as e:
                self.error_message(
                    f"Unable to update added transaction {transaction['transaction_id']}: {e}"
                )

        self.success_message(
            f"Updated {len(added) - len(uncategorized_transactions)} added transactions"
        )

        if len(uncategorized_transactions) > 0:
            self.warning_message(
                f"Unable to categorize {len(uncategorized_transactions)} added transactions"
            )

    def handle_removed_transactions(self, removed, category_map):
        """
        Remove the transactions from the database
        """
        for transaction in removed:
            try:
                transaction_hash = self.generate_unique_hash(
                    transaction["transaction_id"]
                )
                Transaction.objects.filter(hash=transaction_hash).delete()
            except Exception as e:
                self.error_message(
                    f"Unable to delete removed transaction {transaction['transaction_id']}: {e}"
                )

    def handle(self, *args, **options):
        # If the transactions table is empty, return
        if not Transaction.objects.exists():
            self.warning_message("Transactions table is empty.")
            self.warning_message(
                "Run `python manage.py seedtransactions` to populate the transactions."
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
        added = []
        modified = []
        removed = []

        # Retrieve all categories mapped with keys of detailed_name and values of id
        categories = Category.objects.all()
        category_map = {category.detailed_name: category.id for category in categories}

        def fetch_transactions_sync(access_token, next_cursor=None):
            """
            Retrieve Transactions Sync
            """
            if next_cursor:
                request = TransactionsSyncRequest(
                    access_token=PLAID_ACCESS_TOKEN,
                    cursor=next_cursor,
                )
            else:
                request = TransactionsSyncRequest(access_token=access_token)

            return plaid_client.transactions_sync(request).to_dict()

        # For each item in the database, fetch the transactions history
        for item in Item.objects.all():
            # Use the last persisted cursor or "" for fetching all historical transactions
            last_cursor = item.transactions_cursor
            if last_cursor is not None:
                response = fetch_transactions_sync(PLAID_ACCESS_TOKEN, last_cursor)
            else:
                response = fetch_transactions_sync(PLAID_ACCESS_TOKEN)

            added.extend(response["added"])
            modified.extend(response["modified"])
            removed.extend(response["removed"])
            has_more = response["has_more"]
            next_cursor = response["next_cursor"]

            while has_more:
                response = fetch_transactions_sync(PLAID_ACCESS_TOKEN, next_cursor)
                added.extend(response["added"])
                modified.extend(response["modified"])
                removed.extend(response["removed"])
                has_more = response["has_more"]
                next_cursor = response["next_cursor"]

            self.success_message(f"Added: {len(added)}")
            self.success_message(f"Modified: {len(modified)}")
            self.success_message(f"Removed: {len(removed)}")

            added.extend(modified)
            self.handle_added_and_modified_transactions(added, category_map)
            self.handle_removed_transactions(removed, category_map)

            item.transactions_cursor = next_cursor
            item.save()

            # Clear the accounts_map for the next item
            self.accounts_map = {}
            self.success_message("Transactions update complete")
