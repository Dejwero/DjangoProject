from django.contrib import admin
from .models import Profile, Image, Like, Comment

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'age', 'bio', 'status']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['description', 'profile']
    inlines = [CommentInline]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'image']
