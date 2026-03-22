# 🎬 CineLog – Personal Film Rating App

A full-stack web application built with Django that allows users to discover, track, and rate movies using the OMDb API.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Roadmap](#roadmap)

---

## About

CineLog is a personal movie tracking and rating application. Users can search for films via the OMDb API, add them to their personal watchlist, rate them, and leave comments. Each user has their own private film collection and a customizable profile page.

This project was built as a learning exercise to cover all core Django fundamentals, including Models, Views, Templates, Authentication, ORM, Migrations, and API integration.

---

## Features

### 🎥 Movies
- Search for movies via the **OMDb API** with multiple results
- View detailed movie information (plot, cast, director, awards, runtime)
- Add movies to your personal list with one click
- Delete movies from your list
- Prevent duplicate entries per user

### ⭐ Reviews
- Rate movies on a scale of 0.0 – 10.0
- Leave personal comments for each movie
- View and update your ratings at any time
- Personal ratings displayed on the movie list

### 🔐 Authentication
- User registration and login
- Secure logout
- Protected routes – only authenticated users can add or delete movies
- Each user has their own private film collection

### 👤 User Profile
- Customizable profile with bio, favorite genre, favorite movie, favorite actor, and favorite director
- Profile picture upload
- Profile accessible via navigation avatar

### 🔍 Search
- Search the OMDb database for new movies to add
- Search within your personal movie list
- Inline search bar on the movie list page

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0 |
| Database | MySQL 8.0 |
| Frontend | Django Templates + Custom CSS |
| External API | OMDb API |
| Authentication | Django Built-in Auth |
| Image Handling | Pillow |
| Environment | python-dotenv |
| HTTP Requests | requests |

---

## Project Structure

```
cinelog/
├── cinelog/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── movies/                   # Movies & Reviews app
│   ├── migrations/
│   ├── templates/
│   │   └── movies/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── add.html
│   │       ├── search.html
│   │       ├── detail.html
│   │       ├── temp_detail.html
│   │       └── my_list_search.html
│   ├── models.py             # Movie & Review models
│   ├── views.py              # All movie views
│   ├── urls.py               # Movie URL patterns
│   ├── utils.py              # OMDb API helper functions
│   └── admin.py
├── users/                    # Authentication & Profiles app
│   ├── migrations/
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── users/
│   │       └── profile.html
│   ├── models.py             # UserProfile model
│   ├── views.py              # Register & Profile views
│   ├── urls.py               # User URL patterns
│   └── context_processors.py
├── media/                    # User uploaded files
├── .env                      # Environment variables (not tracked)
├── .gitignore
├── requirements.txt
└── manage.py
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL 8.0+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/CineLog-Django-App.git
cd CineLog-Django-App
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory (see [Environment Variables](#environment-variables))

**5. Create the MySQL database**
```sql
CREATE DATABASE cinelog;
```

**6. Run migrations**
```bash
python manage.py migrate
```

**7. Create a superuser**
```bash
python manage.py createsuperuser
```

**8. Start the development server**
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=cinelog
DB_USER=your-mysql-username
DB_PASSWORD=your-mysql-password
DB_HOST=localhost
DB_PORT=3306
OMDB_API_KEY=your-omdb-api-key
```

You can get a free OMDb API key at [https://www.omdbapi.com/apikey.aspx](https://www.omdbapi.com/apikey.aspx)

---

## Usage

### Searching for Movies
1. Click **"+ Film hinzufügen"** in the navigation
2. Enter a movie title in the search bar
3. Browse the results with posters
4. Click on a movie to see full details
5. Click **"+ Zu meiner Liste hinzufügen"** to add it

### Rating a Movie
1. Go to **"Meine Filme"**
2. Click on any movie in your list
3. Enter a rating (0.0 – 10.0) and an optional comment
4. Click **"Bewertung speichern"**

### Managing your Profile
1. Click on your username or avatar in the navigation
2. Fill in your profile details
3. Upload a profile picture
4. Click **"Profil speichern"**

---

## Roadmap

- [ ] Sort movies by rating, year, or genre
- [ ] Pagination for large movie lists
- [ ] Password change functionality
- [ ] Password reset via email
- [ ] Deployment to production

---

## License

This project is for educational purposes. Movie data is provided by the [OMDb API](https://www.omdbapi.com/).
