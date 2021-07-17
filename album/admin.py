from django.contrib import admin
from .models import Photo, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    '''Comment admin model.'''
    model = Comment
    extra = 1

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    '''Photo admin model.'''
    inlines = [
        CommentInline,
    ]
    
    list_display = ("title", "approved")
    list_filter = ('created_at', 'approved', 'submitter')
