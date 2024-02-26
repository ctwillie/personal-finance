from django.db import models


class Item(models.Model):
    plaid_item_id = models.CharField(max_length=255, null=True, unique=True)
    plaid_institution_id = models.CharField(max_length=255, null=True)
    transactions_cursor = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.plaid_institution_id, self.plaid_item_id)


class Account(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    plaid_account_id = models.CharField(max_length=255, null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    official_name = models.CharField(max_length=255, null=True)
    mask = models.CharField(max_length=255, null=True)
    subtype = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.plaid_account_id)


class Category(models.Model):
    primary_name = models.CharField(max_length=255)
    detailed_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.primary_name, self.detailed_name)


class Transaction(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    plaid_transaction_id = models.CharField(max_length=255, null=True)
    hash = models.CharField(max_length=255, null=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.amount, self.plaid_transaction_id)
