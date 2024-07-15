
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class RegisterTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='example7',
            password='examplepassword'
        )

    def test_register_user(self):
        data = {
            "username": "example7",
            "password": "examplepassword",
            "email": "example@example.com",
            "password2": "examplepassword"}
        response = self.client.post(reverse('register'), data=data)
        assert response.status_code == status.HTTP_200_OK

    def test_token_obtaining(self):
        data = {"username": "example7", "password": "examplepassword"}
        response = self.client.post(reverse('token_obtain_pair'), data=data)
        assert response.status_code == status.HTTP_200_OK

    def test_token_refresh(self):
        refresh = RefreshToken.for_user(self.user)
        data = {"username": "example7", "password": "examplepassword", "refresh": str(refresh)}
        response = self.client.post(reverse('token_refresh'), data=data)
        assert response.status_code == status.HTTP_200_OK

