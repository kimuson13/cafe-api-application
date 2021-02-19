from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@test.com', password='testpass'):
    """Create sample user"""

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""

        email = 'test@test.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_noramalized(self):
        """Test the email for a new user is noramlized"""

        email = 'test@TEST.COM'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_creaet_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'testsuper@test.com',
            'testpass'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Home roasting'
        )

        self.assertEqual(str(tag), tag.name)
