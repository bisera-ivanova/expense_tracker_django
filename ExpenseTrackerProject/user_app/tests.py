import unittest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegisterTestCase(APITestCase):

    def test_register_user(self):
        data = {
            "username": "example7",
            "password": "examplepassword",
            "email": "example@example.com",
            "password2": "examplepassword"}
        response = self.client.post(reverse('register', data
                                            ))
        assert response.status_code == status.HTTP_201_CREATED


if __name__ == '__main__':
    unittest.main()
