from rest_framework import serializers
from trackr.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
    def __str__(self):
        return self.name
