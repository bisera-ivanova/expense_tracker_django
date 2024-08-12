import unittest

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from trackr.models import Expense


class ExpenseCreateTestCase(APITestCase):

    def setUp(self):
        username = 'admintestuser'
        password = 'testpassword'
        self.user = User.objects.create_user(username=username, password=password, is_active=True)
        resp = self.client.post(reverse("token_obtain_pair"),
                                {'username': username, 'password': password},
                                format='json')
        self.token = resp.data['access']

    def test_create_expense(self):
        expense_data = {
            'name': 'groceries',
            'amount': 100,
            'date': '2022-12-31',
            'description': 'Buying fresh vegetables'
        }
        url = reverse('expense_create')
        headers = {'Authorization': f'Bearer {self.token}'}
        response = self.client.post(url, headers=headers, data=expense_data)
        assert response.status_code == status.HTTP_201_CREATED


class ExpenseListTestCase(APITestCase):

    def setUp(self):
        username = 'testuser'
        password = 'testpassword'
        self.user = User.objects.create_superuser(username=username, password=password, is_active=True, is_staff=True)
        resp = self.client.post(reverse("token_obtain_pair"),
                                data={'username': username, 'password': password},
                                format='json')
        self.client.force_login(user=self.user)
        self.token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        Expense.objects.create(name='groceries', amount=100, description='Buying fresh vegetables',
                               expense_creator=self.user)
        Expense.objects.create(name='rent', amount=1500, description='Monthly rent', expense_creator=self.user)

    def test_list_expenses_get(self):
        url = reverse("all_expenses")
        response = self.client.get(url)
        print(response.content)
        assert response.status_code == status.HTTP_200_OK


class ExpenseDetailTestCase(APITestCase):
    pass


if __name__ == '__main__':
    unittest.main()
