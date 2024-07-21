from django.contrib import admin
from .models import Post, Comment, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'like_count')
    search_fields = ('title', 'content')
    list_filter = ('published_date', 'author')
    ordering = ('-published_date',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_date')
    search_fields = ('text',)
    list_filter = ('created_date', 'author')
    ordering = ('-created_date',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('post', 'user')
    list_filter = ('post', 'user')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
