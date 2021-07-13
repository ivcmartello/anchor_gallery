from django.contrib import admin
from .models import Photo, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    
    list_display = ("title", "approved")
