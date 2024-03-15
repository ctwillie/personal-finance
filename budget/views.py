from datetime import date
from django.db.models import Count, F, Sum
from inertia import inertia

from budget.models import Transaction


@inertia("Budget/Index")
def index(request):
    return {}


@inertia("Budget/Dashboard")
def dashboard(request):
    today = date.today()
    current_month = today.strftime("%B")
    current_date = today.strftime("%m/%d/%Y")

    # Monthly Transaction Stats
    monthly_transactions = Transaction.objects.filter(
        date__year=today.year, date__month=today.month, amount__gt=0
    )
    total_spend = sum([transaction.amount for transaction in monthly_transactions])
    greater_than_100 = monthly_transactions.filter(amount__gt=100).count()
    average_daily_spend = total_spend / today.day

    # Monthly Category Stat
    spend_by_category_results = (
        Transaction.objects.filter(
            date__year=today.year, date__month=today.month, amount__gt=0
        )
        .values(category_name=F("category__primary_name"))
        .annotate(spend=Sum("amount"))
        .order_by("-spend")
    )

    spend_by_category = list(spend_by_category_results.all())
    for category in spend_by_category:
        category_percentage = (category["spend"] / total_spend) * 100
        formatted_category = category["category_name"].replace("_", " ").title()

        category["value"] = float(category["spend"])
        category["name"] = formatted_category + f" ({category_percentage:.2f}%)"

    # Number of Transactions by Day
    transactions_by_day_results = (
        Transaction.objects.filter(
            date__year=today.year, date__month=today.month, amount__gt=0
        )
        .values("date")
        .annotate(total_transactions=Count("id"))
        .order_by("date")
    )
    transactions_by_day = list(transactions_by_day_results.all())
    for day in transactions_by_day:
        day["date"] = day["date"].strftime("%m/%d")
        day["Total Transactions"] = day["total_transactions"]

    return {
        "currentDate": current_date,
        "currentMonth": current_month,
        "monthlyTransactions": monthly_transactions,
        "monthlySpendByCategory": spend_by_category,
        "monthlyTransactionsByDay": transactions_by_day,
        "overviewStats": [
            {
                "name": "Total Transactions",
                "value": monthly_transactions.count(),
            },
            {
                "name": "Total Spent",
                "value": f"${total_spend:.2f}",
            },
            {
                "name": "Greater Than $100",
                "value": greater_than_100,
            },
            {
                "name": "Average Daily Spend",
                "value": f"${average_daily_spend:.2f}",
            },
        ],
    }


@inertia("Budget/Transactions")
def transactions_index(request):
    transactions_result = (
        Transaction.objects.select_related("category")
        .filter(amount__gt=0)
        .order_by("-date")
        .all()[:100]
    )

    amount_total = sum([transaction.amount for transaction in transactions_result])
    transactions = []

    # TODO: The loaded category is not sent in the serialized response
    #      Investigate serializers and determine why the category is not being sent
    #      In the meantime, I'm manually adding the categor.primary_name to the response
    for transaction in transactions_result:
        transactions.append(
            {
                "id": transaction.id,
                "date": transaction.date,
                "description": transaction.description,
                "category": transaction.category.primary_name,
                "amount": transaction.amount,
            }
        )

    return {
        "transactions": transactions,
        "amountTotal": amount_total,
    }
