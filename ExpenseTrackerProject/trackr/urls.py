from django.contrib import admin
from django.urls import path

from .views import ExpenseList, ExpenseDetail, ExpenseCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ExpenseList.as_view(),
         name='all_expenses'),
    path('expense/<int:pk>', ExpenseDetail.as_view(), name='expense_detail'),
    path("create_expense", ExpenseCreate.as_view(), name='expense_create'),

]
