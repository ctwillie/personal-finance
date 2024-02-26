import os

from django.db import IntegrityError
from django.core.management.base import BaseCommand

import plaid
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest

from budget.models import Account, Item


class Command(BaseCommand):
    help = "Seeds the database with transactions"

    def handle(self, *args, **options):
        # If the items table is not empty, return
        if Item.objects.exists() or Account.objects.exists():
            self.stdout.write(
                self.style.WARNING("Items/Accounts table is not empty. Exiting.")
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

        request = AccountsGetRequest(access_token=PLAID_ACCESS_TOKEN)
        response = plaid_client.accounts_get(request).to_dict()
        item_response = response["item"]
        accounts_response = response["accounts"]

        try:
            item = Item.objects.create(
                plaid_item_id=item_response["item_id"],
                plaid_institution_id=item_response["institution_id"],
            )

            for account in accounts_response:
                Account.objects.create(
                    item=item,
                    plaid_account_id=account["account_id"],
                    name=account["name"],
                    official_name=account["official_name"],
                    mask=account["mask"],
                    subtype=account["subtype"],
                    type=account["type"],
                )
        except Exception as e:
            if type(e) == IntegrityError:
                self.stdout.write(
                    self.style.WARNING(
                        f"Item {item_response['item_id']} already exists in the database"
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(
                        f"Unable to add item {item_response['item_id']} to the database: {e}"
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(f"Added item {item_response['item_id']} to the database")
        )
