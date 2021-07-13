from django.urls import path
from .views import LikeView

app_name = 'api'

urlpatterns = [
    path('like_photo', LikeView.as_view()),
]