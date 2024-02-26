import os
import csv

from django.core.management.base import BaseCommand, CommandError

from budget.models import Category


class Command(BaseCommand):
    help = "Seeds the database with categories"

    def handle(self, *args, **options):
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "categories.csv"
        )

        with open(file_path, "r") as file:
            for row in csv.DictReader(file):
                Category.objects.create(
                    primary_name=row["PRIMARY"],
                    detailed_name=row["DETAILED"],
                    description=row["DESCRIPTION"],
                )

        self.stdout.write(
            self.style.SUCCESS("Successfully seeded the database with categories")
        )
