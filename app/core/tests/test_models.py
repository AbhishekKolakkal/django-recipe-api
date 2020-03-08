from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_with_user_successfull(self):
        """Test Creating a user with successfull email"""
        email = 'kolakkalabhishek6@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_is_normalized(self):
        email = 'kolakkalabhishek6@gmail.com'
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalied_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def creat_new_super_user(self):
        user = get_user_model().objects.create_user(
            'kolakkalabhishek6@gmail.com',
            'test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)