from django import template
from album.models import Like

register = template.Library()

@register.simple_tag
def is_liked(request, uuid):
    # Check if a photo is liked by the user

    user_ip = request.META.get('REMOTE_ADDR')
    is_liked = Like.objects.filter(user_ip=user_ip, photo_uuid=uuid).exists()

    return not is_liked