from django import template
from album.models import Like
from album.helpers import get_client_ip

register = template.Library()

@register.simple_tag
def is_liked(request, uuid):
    # Check if a photo is liked by the user

    user_ip = get_client_ip(request)
    is_liked = Like.objects.filter(user_ip=user_ip, photo=uuid).exists()

    return not is_liked