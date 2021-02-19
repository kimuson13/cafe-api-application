from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from cafe.serializers import TagSerializer


TAGS_URL = reverse('cafe:tag-list')


class PublicTagsAPITests(TestCase):
    """Test the publicly available tags API"""

    def setUp(self):
        