from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from django.utils import timezone

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-published_date')  # Order posts by date
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        if not Post.objects.filter(id=post_id).exists():
            raise NotFound('The post does not exist.')
        return Comment.objects.filter(post_id=post_id).order_by('-created_date')
    
    def post(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        if not Post.objects.filter(id=post_id).exists():
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        return super().post(request, *args, **kwargs)
    
class LikePostAPIView(generics.GenericAPIView):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            return Response({"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
