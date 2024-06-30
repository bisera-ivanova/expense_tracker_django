from .serializers import ExpenseSerializer
from trackr.models import Expense
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ExpenseList(APIView):

    def get(self, request, *args, **kwargs):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        expense_type = request.GET.get('expense_type')

        if not start_date or not end_date or not expense_type:
            expenses = Expense.objects.all()
            serializer = ExpenseSerializer(expenses, many=True)
            return Response({'expenses': serializer.data}, status=status.HTTP_200_OK)

        try:
            expenses = Expense.objects.filter(date__range=[start_date, end_date])
            serializer = ExpenseSerializer(expenses, many=True)
            return Response({'expenses': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExpenseDetail(APIView):
    def get(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def post(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return Response(status=204)


class ExpenseCreate(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
