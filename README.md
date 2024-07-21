# Blog-Task

Django Blog API: 

This is a Django application for a blog with token-based authentication using JWT. 
It includes endpoints for managing posts and comments.

Table of Contents:

Requirements => 

Python 3.8+
Django 4.2+
Django REST Framework
djangorestframework-simplejwt
Setup and Installation
Clone the Repository

bash
Copy code
git clone https://github.com/anshuman2197/Blog-Task.git
cd your_repository
Create a Virtual Environment

bash
Copy code
python -m venv env
Activate the Virtual Environment

On Windows:

bash
Copy code
env\Scripts\activate
On macOS/Linux:

bash
Copy code
source env/bin/activate
Install Requirements

bash
Copy code
pip install -r requirements.txt
Apply Migrations

bash
Copy code
python manage.py migrate
Create a Superuser (optional, for admin access)

bash
Copy code
python manage.py createsuperuser
Running the Application
Start the Development Server

bash
Copy code
python manage.py runserver
Access the Application

Open your browser and go to http://127.0.0.1:8000/.

API Documentation
Authentication
Obtain Token

URL: /api/token/

Method: POST

Body:

json
Copy code
{
    "username": "your_username",
    "password": "your_password"
}
Response:

json
Copy code
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
Refresh Token

URL: /api/token/refresh/

Method: POST

Body:

json
Copy code
{
    "refresh": "your_refresh_token"
}
Response:

json
Copy code
{
    "access": "new_access_token"
}
Post Endpoints
List/Create Posts

URL: /api/posts/

Method: GET (List) / POST (Create)

Headers: Authorization: Bearer <your_jwt_token>

Request Body (for POST):

json
Copy code
{
    "title": "Post Title",
    "content": "Post Content",
    "published_date": "2024-07-21T12:00:00Z"
}
Response (for GET):

json
Copy code
[
    {
        "id": 1,
        "title": "Post Title",
        "content": "Post Content",
        "author": "username",
        "published_date": "2024-07-21T12:00:00Z"
    }
]
Retrieve/Update/Delete Post

URL: /api/posts/<int:pk>/

Method: GET (Retrieve) / PUT (Update) / DELETE (Delete)

Headers: Authorization: Bearer <your_jwt_token>

Request Body (for PUT):

json
Copy code
{
    "title": "Updated Post Title",
    "content": "Updated Post Content",
    "published_date": "2024-07-21T12:00:00Z"
}
Response (for GET):

json
Copy code
{
    "id": 1,
    "title": "Post Title",
    "content": "Post Content",
    "author": "username",
    "published_date": "2024-07-21T12:00:00Z"
}
Comment Endpoints
List/Create Comments for a Post

URL: /api/posts/<int:post_id>/comments/

Method: GET (List) / POST (Create)

Headers: Authorization: Bearer <your_jwt_token>

Request Body (for POST):

json
Copy code
{
    "text": "Comment Text"
}
Response (for GET):

json
Copy code
[
    {
        "id": 1,
        "post": 1,
        "author": "username",
        "text": "Comment Text",
        "created_date": "2024-07-21T12:00:00Z"
    }
]
Examples
Obtain Token
Request:

bash
Copy code
curl -X POST http://127.0.0.1:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
Response:

json
Copy code
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
Create a Post
Request:

bash
Copy code
curl -X POST http://127.0.0.1:8000/api/posts/ \
     -H "Authorization: Bearer your_access_token" \
     -H "Content-Type: application/json" \
     -d '{"title": "New Post", "content": "This is the content of the new post.", "published_date": "2024-07-21T12:00:00Z"}'
Response:

json
Copy code
{
    "id": 1,
    "title": "New Post",
    "content": "This is the content of the new post.",
    "author": "username",
    "published_date": "2024-07-21T12:00:00Z"
}
