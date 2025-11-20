# Django Social Website

A social image-sharing app built with Django 5. Users can register, log in, manage profiles, bookmark images from the internet, follow others, and like shared content. The project focuses on practical social features built on top of Django’s authentication system.

## Features

- User registration, login, logout, password reset, password change
- Profile editing with an extended user model
- Bookmark and share images from external sources
- Like/unlike images
- Follow users and view a personalized activity dashboard
- Media upload support for user content

## Setup

Clone the repository:

```
git clone https://github.com/mario-ak37/social-website.git
cd social-website
```

Install dependencies using **uv**:

```
uv sync
```

Run migrations and start the server:

```
python manage.py migrate
python manage.py runserver
```
