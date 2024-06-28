from .serializers import ExpenseSerializer
from trackr.models import Expense
from rest_framework.views import APIView
from rest_framework.response import Response


class ExpenseList(APIView):

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
