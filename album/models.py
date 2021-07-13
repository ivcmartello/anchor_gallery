from django.db import models
from .helpers import get_client_ip

import uuid

# Create your models here.

class Like(models.Model):
    user_ip = models.CharField(max_length=50)
    photo_uuid = models.UUIDField(default=uuid.uuid4, editable=True)
    created_at = models.DateTimeField(auto_now_add=True) 


class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=300)
    image = models.ImageField()
    approved = models.BooleanField(default=False)
    submitter = models.CharField(max_length=100)

    def like_manager(self, request):
        user_ip = get_client_ip(request)
        like_obj = Like.objects.filter(photo_uuid=self.uuid, user_ip=user_ip)

        liked = False
        if like_obj.exists():
            like_obj.first().delete()
        else:
            Like.objects.create(photo_uuid=self.uuid, user_ip=user_ip)
            liked = True

        return liked, self.like_count

    # Number of likes
    @property
    def like_count(self):
        return Like.objects.only('photo_uuid').filter(photo_uuid=self.uuid).count()


class Comment(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ForeignKey(Photo, related_name="comments", on_delete=models.CASCADE)
