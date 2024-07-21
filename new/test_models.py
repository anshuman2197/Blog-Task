from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from django.utils import timezone

class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            published_date=timezone.now()
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')

class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            published_date=timezone.now()
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text='This is a test comment.'
        )

    def test_comment_str(self):
        self.assertEqual(
            str(self.comment),
            f'Comment by {self.comment.author.username} on "Test Post": This is a test comment.'
        )
