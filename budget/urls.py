from django.urls import path
from .views import budget as budget_view, transactions as transactions_view

app_name = "budget"

urlpatterns = [
    path("", budget_view.dashboard, name="index"),
    path("transactions", transactions_view.index, name="transactions.index"),
    path("transactions/list", transactions_view.list, name="transactions.list"),
]
