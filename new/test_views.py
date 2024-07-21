from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post, Comment
from django.utils import timezone

class PostAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            published_date=timezone.now()
        )
    
    def test_list_posts(self):
        url = reverse('post-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response contains the post we created
        self.assertEqual(len(response.data), 1)  # Assuming PAGE_SIZE is 10 and we only have 1 post

    def test_create_post(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'This is a new post.', 'published_date': timezone.now().isoformat()}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_update_post(self):
        url = reverse('post-retrieve-update-destroy', args=[self.post.id])
        data = {'title': 'Updated Title', 'content': 'Updated content.', 'published_date': self.post.published_date.isoformat()}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated content.')

    def test_delete_post(self):
        url = reverse('post-retrieve-update-destroy', args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_list_posts(self):
        url = reverse('post-list-create')
        response = self.client.get(url)
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Adjust to check 'results'


    def test_unlike_post(self):
        url = reverse('like-post', args=[self.post.id])
        self.client.post(url)  # Like the post first
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.post.likes.count(), 0)

class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            published_date=timezone.now()
        )
        self.client.force_authenticate(user=self.user)

    def test_create_comment(self):
        url = reverse('comment-list-create', args=[1])  # Replace with correct URL for comment creation
        data = {
            'text': 'This is a new comment.',
            'post': 1,  # Ensure this ID corresponds to an existing post
            'author': self.user.pk,  # Assuming `author` should be the current user; adjust as needed
        }
        response = self.client.post(url, data, format='json')
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




    def test_create_comment_for_nonexistent_post(self):
        url = reverse('comment-list-create', args=[999])  # Non-existent post ID
        data = {'text': 'This is a new comment.'}
        response = self.client.post(url, data, format='json')
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



    def test_list_comments(self):
        Comment.objects.create(post=self.post, author=self.user, text='Comment 1')
        Comment.objects.create(post=self.post, author=self.user, text='Comment 2')
        url = reverse('comment-list-create', args=[self.post.id])
        response = self.client.get(url)
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)  # Adjust to check 'results'



    def tearDown(self):
        self.client.logout()  # Ensure that the user is logged out after each test
