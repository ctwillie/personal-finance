from datetime import date
from inertia import inertia

from budget.models import Transaction


@inertia("Budget/Index")
def index(request):
    return {}


@inertia("Budget/Dashboard")
def dashboard(request):
    today = date.today()
    currentMonth = today.strftime("%B")
    currentDate = today.strftime("%m/%d/%Y")

    monthlyTransactions = Transaction.objects.filter(
        date__year=today.year, date__month=today.month, amount__gt=0
    )
    totalSpent = sum([transaction.amount for transaction in monthlyTransactions])
    greaterThan100 = monthlyTransactions.filter(amount__gt=100).count()
    averageDailySpend = totalSpent / monthlyTransactions.count()

    return {
        "currentDate": currentDate,
        "currentMonth": currentMonth,
        "monthlyTransactions": monthlyTransactions,
        "overviewStats": [
            {
                "name": "Total Transactions",
                "value": monthlyTransactions.count(),
            },
            {
                "name": "Total Spent",
                "value": f"${totalSpent:.2f}",
            },
            {
                "name": "Greater Than $100",
                "value": greaterThan100,
            },
            {
                "name": "Average Daily Spend",
                "value": f"${averageDailySpend:.2f}",
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
