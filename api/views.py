from rest_framework.views import APIView
from django.http import JsonResponse
from album.models import Photo

# Create your views here.

class LikeView(APIView):
  
    """ Like or dislike photos."""
    def get(self, request):
        photo_uuid = request.GET.get('photo_uuid', '')
        photo = Photo.objects.filter(pk=photo_uuid)
        
        liked = False
        like_count = 0
        if photo.exists():
            liked, like_count = photo.first().like_manager(request)
            
        return JsonResponse({'liked': liked, 'like_count': like_count})
