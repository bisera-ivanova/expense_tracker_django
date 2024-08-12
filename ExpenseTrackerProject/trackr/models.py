from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = (
        ('GROCERIES', 'Groceries'),
        ('LEISURE', 'Leisure'),
        ('ELECTRONICS', 'Electronics'),
        ('UTILITIES', 'Utilities'),
        ('CLOTHING', 'Clothing'),
        ('HEALTH', "Health"),
        ('OTHER', "Other")
    )
    expense_creator = models.ForeignKey(User, on_delete=models.CASCADE, db_column="expense_creator")
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    type = models.CharField(choices=EXPENSE_TYPE_CHOICES, default='OTHER', max_length=20)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
