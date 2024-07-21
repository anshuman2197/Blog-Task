from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    LikePostAPIView
)

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:post_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='like-post'),
]
