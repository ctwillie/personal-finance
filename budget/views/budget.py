from datetime import date
from inertia import inertia

from budget.services.transaction import TransactionService


@inertia("Budget/Dashboard")
def dashboard(request):
    today = date.today()
    current_month = today.strftime("%B")
    current_date = today.strftime("%m/%d/%Y")
    transaction_service = TransactionService()

    # Monthly Transaction Stats
    monthly_income_transactions = transaction_service.get_monthly_income_transactions()
    monthly_transactions = transaction_service.get_monthly_transactions()
    monthly_spend_by_category = transaction_service.get_monthly_spend_by_category()
    monthly_transactions_by_day = transaction_service.get_monthly_transactions_by_day()
    monthly_recent_transactions = transaction_service.get_monthly_recent_transactions()
    monthly_transaction_amount_by_day = (
        transaction_service.get_monthly_transaction_amount_by_day()
    )

    # Overview Stats
    gross_income = sum(
        [abs(transaction.amount) for transaction in monthly_income_transactions]
    )
    total_expenses = sum(
        [transaction["amount"] for transaction in monthly_transactions]
    )
    net_income = gross_income - total_expenses

    average_daily_spend = total_expenses / today.day

    # Format Monthly Category Stat
    for category in monthly_spend_by_category:
        category_percentage = (category["spend"] / total_expenses) * 100
        formatted_category = category["category_name"].replace("_", " ").title()

        category["value"] = float(category["spend"])
        category["name"] = formatted_category + f" ({category_percentage:0.2f}%)"

    # Format Number of Transactions by Day
    for day in monthly_transactions_by_day:
        day["date"] = day["date"].strftime("%-m/%d")
        day["Total Transactions"] = day["total_transactions"]

    # Format Transaction Amount by Day
    for day in monthly_transaction_amount_by_day:
        day["date"] = day["date"].strftime("%-m/%d")
        day["Total Amount"] = float(day["daily_amount"])

    # Format Monthly Recent Transactions
    for recent_transaction in monthly_recent_transactions:
        recent_transaction["date"] = recent_transaction["date"].strftime("%-m/%d")
        recent_transaction["amount"] = float(recent_transaction["amount"])
        category_name = recent_transaction["category_name"].replace("_", " ").title()
        recent_transaction["category_name"] = (
            category_name if len(category_name) <= 40 else category_name[:40] + "..."
        )

    return {
        "currentDate": current_date,
        "currentMonth": current_month,
        "monthlyTransactions": monthly_transactions,
        "monthlySpendByCategory": monthly_spend_by_category,
        "monthlyTransactionsByDay": monthly_transactions_by_day,
        "monthlyTransactionAmountByDay": monthly_transaction_amount_by_day,
        "monthlyTotalTransactions": len(monthly_transactions),
        "monthlyRecentTransactions": monthly_recent_transactions,
        "overviewStats": [
            {
                "name": "Gross Income",
                "value": f"${gross_income:0,.2f}",
            },
            {
                "name": "Total Expenses",
                "value": f"${total_expenses:0,.2f}",
            },
            {
                "name": "Net Income",
                "value": f"${net_income:0,.2f}",
            },
            {
                "name": "Average Daily Spend",
                "value": f"${average_daily_spend:0,.2f}",
            },
        ],
    }
