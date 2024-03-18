from django.urls import path
from . import views

app_name = "budget"

urlpatterns = [
    path("", views.dashboard, name="index"),
    path("transactions", views.transactions_index, name="transactions.index"),
]
