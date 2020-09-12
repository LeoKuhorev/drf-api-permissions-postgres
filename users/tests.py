from django.contrib.auth.models import AnonymousUser
from django.db.utils import IntegrityError
from django.test import RequestFactory, TestCase

from .models import CustomUser
from .views import profile


class TestCustomUer(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(
            username='testUser',
            email='test_user@company.com',
            first_name='test_name',
            last_name='test_last_name',
            date_of_birth='1990-01-01',
            password='test_password_123')
        self.user.save()

    def test_user_saved(self):
        saved_user = CustomUser.objects.last()
        self.assertEqual(self.user, saved_user)

    def test_cannot_save_same_email(self):
        with self.assertRaises(Exception) as raised:
            new_user = CustomUser.objects.create_user(
                username='test_new_user',
                email='test_user@company.com',
                first_name='test_new_name',
                last_name='test_new_last_name',
                date_of_birth='1990-01-01',
                password='test_password_123')
            new_user.save()
        self.assertEqual(IntegrityError, type(raised.exception))

    def test_profile_page_logged_in_user_success(self):
        # Create an instance of a GET request.
        request = self.factory.get('/user/profile')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_page_anon_user_fail(self):
        # Create an instance of a GET request.
        request = self.factory.get('/user/profile')
        request.user = AnonymousUser()
        response = profile(request)
        self.assertEqual(response.status_code, 302)
