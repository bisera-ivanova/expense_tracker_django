from rest_framework import serializers
from trackr.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    expense_creator = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'

    def __str__(self):
        return self.name
