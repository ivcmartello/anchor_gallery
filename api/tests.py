import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from album.models import Photo
from .views import LikeView


class TestLikeView(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.photo = Photo.objects.create(title='Big', approved=True)

    def test_like_view(self):
        request = self.factory.get('api/like_photo/', {'photo_uuid': self.photo.uuid})
        view = LikeView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'liked': True, 'like_count': 1})