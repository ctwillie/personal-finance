from django.shortcuts import render

from budget.models import Transaction


def index(request):
    return render(request, "budget/index.html")


def transactions_index(request):
    transactions = Transaction.objects.select_related("category").all()[:100]

    return render(
        request, "budget/transactions_index.html", {"transactions": transactions}
    )
