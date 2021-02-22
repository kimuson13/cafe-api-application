import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag, Cafe

from cafe.serializers import TagSerializer


TAGS_URL = reverse('cafe:tag-list')


class PublicTagsAPITests(TestCase):
    """Test the publicly available tags API"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login in required for retrieving tags"""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test the authorized user tags API"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'testpass',
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(user=self.user, name='home roasting')
        Tag.objects.create(user=self.user, name='reasnable')

        res = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags returned are for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            'test2@test.com',
            'testpass',
        )
        Tag.objects.create(user=user2, name='Home roasting')
        tag = Tag.objects.create(user=self.user, name='near the station')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {'name': 'famous'}
        self.client.post(TAGS_URL, payload)

        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(TAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_tags_assigned_to_cafes(self):
        """Test filtering tags by those assigned to cafe"""
        tag1 = Tag.objects.create(user=self.user, name='test tag1')
        tag2 = Tag.objects.create(user=self.user, name='test tag2')
        cafe = Cafe.objects.create(
            name='test cafe',
            address='test address',
            opening_time=datetime.time(10),
            close_time=datetime.time(20),
            user=self.user
        )
        cafe.tags.add(tag1)

        res = self.client.get(TAGS_URL, {'assigned_only': 1})

        serializer1 = TagSerializer(tag1)
        serializer2 = TagSerializer(tag2)
        self.assertIn(serializer1.data, res.data)
        self.assertNotIn(serializer2.data, res.data)

    def test_retrieving_tags_assigned_unique(self):
        """Test filtering tags by assigned returns unique items"""
        tag = Tag.objects.create(user=self.user, name='test tag1')
        Tag.objects.create(user=self.user, name='test tag2')
        cafe1 = Cafe.objects.create(
            name='test cafe',
            address='test address',
            opening_time=datetime.time(10, 30),
            close_time=datetime.time(20),
            user=self.user
        )
        cafe1.tags.add(tag)
        cafe2 = Cafe.objects.create(
            name='test cafe2',
            address='test address2',
            opening_time=datetime.time(10),
            close_time=datetime.time(20),
            user=self.user
        )
        cafe2.tags.add(tag)

        res = self.client.get(TAGS_URL, {'assigned_only': 1})

        self.assertEqual(len(res.data), 1)
