from datetime import date
from django.db.models import Count, F, Sum
from budget.models import Transaction


class TransactionService:
    def __init__(self):
        self.today = date.today()

        # Exclude these positive transactions related to transfers
        self.exclude_category_detailed_names = [
            "TRANSFER_OUT_SAVINGS",
            "TRANSFER_OUT_ACCOUNT_TRANSFER",
        ]

    def get_transactions_index(self):
        return (
            Transaction.objects.annotate(category_name=F("category__detailed_name"))
            .values("id", "amount", "date", "category_name")
            .filter(amount__gt=0)
            .order_by("-date")
            .all()[:100]
        )

    def get_monthly_income_transactions(self):
        return Transaction.objects.filter(
            date__year=self.today.year,
            date__month=self.today.month,
            amount__lt=0,
            category__primary_name="INCOME",
        )

    def get_monthly_transactions(self, limit=None):
        monthly_transactions = (
            Transaction.objects.filter(
                date__year=self.today.year,
                date__month=self.today.month,
                amount__gt=0,
            )
            .exclude(
                category__detailed_name__in=self.exclude_category_detailed_names,
            )
            .annotate(categoryName=F("category__detailed_name"))
            .values("id", "amount", "description", "date", "categoryName")
        )

        if limit:
            return list(monthly_transactions.all()[:limit])

        return list(monthly_transactions.all())

    def get_monthly_recent_transactions(self, limit=10):
        recent_trasactions = (
            Transaction.objects.filter(
                date__year=self.today.year,
                date__month=self.today.month,
                amount__gt=0,
            )
            .annotate(category_name=F("category__detailed_name"))
            .values("id", "amount", "date", "category_name")
            .exclude(category__detailed_name__in=self.exclude_category_detailed_names)
            .order_by("-date")[:limit]
        )

        return list(recent_trasactions)

    def get_monthly_spend_by_category(self):
        spend_by_category_results = (
            Transaction.objects.filter(
                date__year=self.today.year,
                date__month=self.today.month,
                amount__gt=0,
            )
            .exclude(
                category__detailed_name__in=self.exclude_category_detailed_names,
            )
            .values(category_name=F("category__primary_name"))
            .annotate(spend=Sum("amount"))
            .order_by("-spend")
        )

        return list(spend_by_category_results.all())

    def get_monthly_transactions_by_day(self):
        transactions_by_day_results = (
            Transaction.objects.filter(
                date__year=self.today.year,
                date__month=self.today.month,
                amount__gt=0,
            )
            .exclude(
                category__detailed_name__in=self.exclude_category_detailed_names,
            )
            .values("date")
            .annotate(total_transactions=Count("id"))
            .order_by("date")
        )

        return list(transactions_by_day_results.all())

    def get_monthly_transaction_amount_by_day(self):
        transactions_by_day_results = (
            Transaction.objects.filter(
                date__year=self.today.year,
                date__month=self.today.month,
                amount__gt=0,
            )
            .exclude(
                category__detailed_name__in=self.exclude_category_detailed_names,
            )
            .values("date")
            .annotate(daily_amount=Sum("amount"))
            .order_by("date")
        )

        return list(transactions_by_day_results)
