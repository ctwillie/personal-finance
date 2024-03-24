from django.http import JsonResponse
from django.core.paginator import Paginator
from inertia import inertia

from budget.services.transaction import TransactionService


@inertia("Budget/Transactions")
def index(request):
    transaction_service = TransactionService()
    transactions = transaction_service.get_monthly_transactions(10)
    amount_total = sum([transaction["amount"] for transaction in transactions])

    # Format Monthly Category Stat
    for transaction in transactions:
        transaction["date"] = transaction["date"].strftime("%-m/%d")
        transaction["categoryName"] = (
            transaction["categoryName"].replace("_", " ").title()
        )

    return {
        "transactions": [],
        "amountTotal": amount_total,
    }


def list(request):
    transaction_service = TransactionService()
    pageIndex = int(request.GET.get("pageIndex", 1)) + 1
    pageSize = int(request.GET.get("pageSize", 10))
    transactions = transaction_service.get_monthly_transactions()

    paginator = Paginator(transactions, pageSize)
    page_count = paginator.num_pages
    transactions = paginator.page(pageIndex).object_list

    # Format Monthly Category Stat
    for transaction in transactions:
        transaction["date"] = transaction["date"].strftime("%-m/%d")
        transaction["categoryName"] = (
            transaction["categoryName"].replace("_", " ").title()
        )

    return JsonResponse(
        {
            "transactions": transactions,
            "pageCount": page_count,
        }
    )
