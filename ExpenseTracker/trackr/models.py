from django.db import models

# Create your models here.


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
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    type = models.CharField(choices=EXPENSE_TYPE_CHOICES, default='OTHER', max_length=20)
    date = models.DateField()
