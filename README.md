# StreamByte

StreamByte is a Django-based movie web application developed as a full-stack web development project. The application provides users with a platform to browse movies, view detailed movie information, save favorites, and interact through comments.

## Overview

The project was developed using Django for the backend, SQLite for data storage, and HTML/CSS for the frontend. It implements user authentication, database relationships, CRUD operations, media handling, and template-based page rendering.

## Features

- User registration and authentication
- Movie listing and detailed movie pages
- Movie categories and ratings
- Actor and release-date information
- Movie trailer links
- Add, edit, and delete movie records
- Favorites management
- Comment creation, editing, and deletion
- Poster and media upload support
- Admin interface for content management
- Responsive web interface

## Technology Stack

**Backend**
- Python
- Django

**Frontend**
- HTML5
- CSS3

**Database**
- SQLite

**Tools**
- Git
- GitHub
- Visual Studio Code

## Application Structure

```text
streambyte/
│
├── manage.py
├── movie_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── movies/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── movie_detail.html
│   ├── favorites.html
│   └── ...
│
├── static/
│   └── style.css
│
├── media/
│   └── posters/
│
├── .gitignore
└── README.md