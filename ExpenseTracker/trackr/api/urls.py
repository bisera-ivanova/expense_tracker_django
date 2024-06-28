from .views import ExpenseList

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_expenses', ExpenseList.as_view(), name='all_expenses'),
]
