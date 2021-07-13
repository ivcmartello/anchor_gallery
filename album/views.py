from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CommentForm
from .models import Photo, Comment


class PhotoListView(ListView):
    model = Photo
    paginate_by = 8   
    template_name = 'album/list.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        """Returns Photos that were approved"""
        return Photo.objects.filter(approved=True).order_by('created_at')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'album/detail.html'
    context_object_name = 'photo'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(photo=self.get_object()).order_by('-created_at')
        data['comment_form'] = CommentForm()

        return data
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            content=request.POST.get('content'), 
            author=request.POST.get('author'), 
            photo=self.get_object()
        )
        new_comment.save()
        
        return redirect(request.META['HTTP_REFERER'])
    

class PhotoCreateView(SuccessMessageMixin, CreateView):
    model = Photo
    fields = ['submitter', 'title', 'image']
    template_name = 'album/create.html'
    success_url = reverse_lazy('photo:list')
    success_message = 'Thanks for your contribution! We will approve as soon as possible!'
