import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Cafe, Tag

from cafe.serializers import CafeSerializer, CafeDetailSerializer


CAFE_URL = reverse('cafe:cafe-list')


def detail_url(cafe_id):
    """Return cafe detail url"""
    return reverse('cafe:cafe-detail', args=[cafe_id])


def sample_tag(user, name='Test tag'):
    """Creat and return a sample tag"""
    return Tag.objects.create(user=user, name=name)


def sample_cafe(user, **params):
    """Create and return a sample cafe"""

    default = {
        'name': 'test cafe',
        'address': 'test-address',
        'opening_time': datetime.time(10),
        'close_time': datetime.time(20),
    }
    default.update()

    return Cafe.objects.create(user=user, **default)


class PublicCafeApiTests(TestCase):
    """Test unauthenticates recipe API access"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authenitcation is required"""
        res = self.client.get(CAFE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateCafeApiTests(TestCase):
    """Test authenticated cafe API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_cafes(self):
        """Test retrieving a list of cafes"""
        sample_tag(user=self.user)

        res = self.client.get(CAFE_URL)

        cafes = Cafe.objects.all().order_by('-id')
        serializer = CafeSerializer(cafes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_cafes_limited_to_user(self):
        """Test retrieving cafes for user"""
        user2 = get_user_model().objects.create_user(
            'test2@test.com',
            'testpass',
        )
        sample_cafe(user=user2)
        sample_cafe(user=self.user)

        res = self.client.get(CAFE_URL)

        cafes = Cafe.objects.filter(user=self.user)
        serializer = CafeSerializer(cafes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    def test_view_cafe_detail(self):
        """Test viewing a cafe detail"""
        cafe = sample_cafe(user=self.user)
        cafe.tags.add(sample_tag(user=self.user))

        url = detail_url(cafe.id)
        res = self.client.get(url)

        serializer = CafeDetailSerializer(cafe)
        self.assertEqual(res.data, serializer.data)

    def test_create_basic_cafe(self):
        """Test creating cafe"""
        payload = {
            'name': 'test cafe',
            'address': 'testaddress-1-1',
            'opening_time': datetime.time(10, 30),
            'close_time': datetime.time(20)
        }
        res = self.client.post(CAFE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        cafe = Cafe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(cafe, key))

    def test_create_cafe_with_tags(self):
        """Test creating a cafe with tags"""
        tag1 = sample_tag(user=self.user, name='home roasting')
        tag2 = sample_tag(user=self.user, name='rich')
        payload = {
            'name': 'test cafe',
            'address': 'testaddress',
            'opening_time': datetime.time(10, 30),
            'close_time': datetime.time(20),
            'tags': [tag1.id, tag2.id]
        }
        res = self.client.post(CAFE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        cafe = Cafe.objects.get(id=res.data['id'])
        tags = cafe.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)

    def test_patial_update_cafe(self):
        """Test updating a cafe with patch"""
        cafe = sample_cafe(user=self.user)
        cafe.tags.add(sample_tag(user=self.user))
        new_tag = sample_tag(user=self.user, name='test new tag')

        payload = {'name': 'new test cafe', 'tags': [new_tag.id]}
        url = detail_url(cafe.id)
        self.client.patch(url, payload)

        cafe.refresh_from_db()
        self.assertEqual(cafe.name, payload['name'])
        tags = cafe.tags.all()
        self.assertEqual(len(tags), 1)
        self.assertIn(new_tag, tags)

    def test_full_update_cafe(self):
        """Test updating a cafe with put"""
        cafe = sample_cafe(user=self.user)
        cafe.tags.add(sample_tag(user=self.user))

        payload = {
            'name': 'renewal test cafe',
            'address': 'newtest address',
            'opening_time': datetime.time(11),
            'close_time': datetime.time(22, 30),
        }
        url = detail_url(cafe.id)
        self.client.put(url, payload)

        cafe.refresh_from_db()
        self.assertEqual(cafe.name, payload['name'])
        self.assertEqual(cafe.address, payload['address'])
        self.assertEqual(cafe.opening_time, payload['opening_time'])
        self.assertEqual(cafe.close_time, payload['close_time'])
        tags = cafe.tags.all()
        self.assertEqual(len(tags), 0)
