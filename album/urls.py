from django.urls import path
from album.views import PhotoListView, PhotoDetailView, PhotoCreateView

app_name = 'photo'

urlpatterns = [
    path("", PhotoListView.as_view(), name="list"),
    path('photo/<uuid:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photo/create/', PhotoCreateView.as_view(), name='create'),
]