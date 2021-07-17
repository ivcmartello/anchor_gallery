from django.db import models
from .helpers import get_client_ip
from sorl.thumbnail import ImageField

import uuid

# Create your models here.

class Photo(models.Model):
    '''Photo model.'''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=300)
    image = ImageField(upload_to="images", blank=True)
    approved = models.BooleanField(default=False)
    submitter = models.CharField(max_length=100)

    def like_manager(self, request):
        '''Like or dislike photo.'''
        user_ip = get_client_ip(request)
        like_obj = self.likes.filter(user_ip=user_ip)

        liked = False
        if like_obj.exists():
            like_obj.first().delete()
        else:
            Like.objects.create(photo=self, user_ip=user_ip)
            liked = True

        return liked, self.like_count

    @property
    def like_count(self):
        '''Number of likes'''
        return self.likes.only('photo').count()


class Like(models.Model):
    '''Like model.'''
    user_ip = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo, related_name="likes", on_delete=models.CASCADE)


class Comment(models.Model):
    '''Comment model.'''
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ForeignKey(Photo, related_name="comments", on_delete=models.CASCADE)
