from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from trackr.models import Expense

from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from .serializers import ExpenseSerializer


class ExpenseList(APIView):
    permission_classes = (AdminOrReadOnly,)

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
    permission_classes = (ReviewUserOrReadOnly,)

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


class ExpenseCreate(CreateAPIView):
    # would not be able to create a new expense unless logged in
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    serializer = ExpenseSerializer(queryset, many=True)

    def perform_create(self, serializer):
        serializer.save(expense_creator=self.request.user)
