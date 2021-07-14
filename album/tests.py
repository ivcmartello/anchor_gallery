from django.test import TestCase, RequestFactory
from django.shortcuts import reverse

from .templatetags.tag_extras import is_liked
from .helpers import get_client_ip
from .forms import CommentForm
from .models import Photo

# Create your tests here.


class TestClientIp(TestCase):
  
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_get_client_ip(self):
        request = self.factory.get('/xyz')
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')
        
        request = self.factory.get('/xyz', HTTP_X_FORWARDED_FOR="8.8.8.8")
        ip = get_client_ip(request)
        self.assertEqual(ip, '8.8.8.8')


class TestLikeManager(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        
    def test_like_manager(self):
        request = self.factory.get('/xyz')
        photo = Photo()
        
        liked, like_count = photo.like_manager(request)
        
        self.assertTrue(liked)
        self.assertEqual(like_count, 1)
        
        request = self.factory.get('/xyz')
        liked, like_count = photo.like_manager(request)
        
        self.assertFalse(liked)
        self.assertEqual(like_count, 0)


class TestIsLikedTag(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        
    def test_islike_tag(self):
        request = self.factory.get('/xyz')
        photo = Photo()
        
        liked = is_liked(request, photo.uuid)
        self.assertTrue(liked)
        
class TestPhotoViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.photo = Photo.objects.create(title='Big', approved=True)
        self.url_list = reverse('photo:list')
        self.url_detail = reverse('photo:detail', kwargs={"pk": self.photo.uuid})

    def test_photo_list_view(self):
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, 200)
        
    def test_get_photo_detail_view(self):
        response = self.client.get(self.url_detail)
        
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['comments'])
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_post_photo_detail_view(self):
        response = self.client.post(self.url_detail, {'content': 'test', 'author': 'Joe'}, HTTP_REFERER=self.url_list)
        
        self.assertEqual(response.status_code, 302)
        
        photo = Photo.objects.filter(pk=self.photo.uuid).first()
        comments = photo.comments.all()
        self.assertIsNotNone(comments)
        self.assertEqual(comments.count(), 1)
        