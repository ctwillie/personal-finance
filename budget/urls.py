from django.urls import path
from . import views

app_name = "budget"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("transactions", views.transactions_index, name="transactions.index"),
]
