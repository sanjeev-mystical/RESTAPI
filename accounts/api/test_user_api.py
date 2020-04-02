from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='restapi', email='shuklasanjeev225@gmail.com')
        user.set_password('ThisISMyNewPwd')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='restapi')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('register')
        data = {
            'username': 'restapi.new',
            'email': 'restapi.new@gmail.com',
            'password': 'newuser'

        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
