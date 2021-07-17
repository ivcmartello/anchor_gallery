from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import CommentForm
from .models import Photo, Comment


class PhotoListView(ListView):
    '''View that shows Photo list.'''
    model = Photo
    paginate_by = 9   
    template_name = 'album/list.html'
    context_object_name = 'photos'
    
    def get_queryset(self):
        '''Returns Photos that were approved'''
        return Photo.objects.filter(approved=True).order_by('-created_at')


class PhotoDetailView(DetailView):
    '''View that shows Photo details.'''
    model = Photo
    template_name = 'album/detail.html'
    context_object_name = 'photo'
    
    def get_context_data(self, **kwargs):
        '''Returns data context injecting Comment Form.'''
        data = super().get_context_data(**kwargs)
        data['comments'] = Comment.objects.filter(photo=self.get_object()).order_by('-created_at')
        data['comment_form'] = CommentForm()

        return data
    
    def post(self, request, *args, **kwargs):
        '''Persist photo comments.'''
        new_comment = Comment(
            content=request.POST.get('content'), 
            author=request.POST.get('author'), 
            photo=self.get_object()
        )
        new_comment.save()
        
        return redirect(request.META['HTTP_REFERER'])
    

class PhotoCreateView(CreateView):
    '''Persist a new photo.'''
    model = Photo
    template_name = 'album/create.html'
    success_url = reverse_lazy('photo:list')
    fields =['submitter', 'title', 'image']