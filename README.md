
# Django Music API (GraphQL)

A backend API built using **Django** and **Graphene-Django** to provide data about  
**Artists, Albums, and Songs** via GraphQL.

This API is part of the Salalem technical task – Part 1.

---

## 🚀 Features

- Django-based backend
- GraphQL API using `graphene-django`
- Models:
  - Artist
  - Album
  - Song
- Queries to fetch:
  - List of artists
  - Lists of albums and songs
- Mutations:
  - Add new artist
- GraphiQL interface for testing queries

---

## 📦 Requirements

- Python 3.10+
- pip
- virtualenv (recommended)

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_NAME/music_backend.git
cd music_backend
### 2. Create virtual environment
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
 ## Required Packages Explanation
### Core Dependencies
 `django` | Web framework | Main backend framework |
pip install -r requirements.txt
| `graphene-django` | GraphQL for Django | Allows React to query data using GraphQL |
| `django-cors-headers` | CORS handling | **CRITICAL**: Allows React (different port) to make requests to Django |
## Configuration Checklist

After installing packages, ensure these are configured:

### ✅ settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Required for React connection
    'corsheaders',        # Must be installed
    'graphene_django',    # Must be installed
    
    # Your apps
    'music',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MUST BE FIRST
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
# CORS Configuration (allows React to connect)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",
    "http://localhost:5177",
]

# For development only - allows all origins
# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

# GraphQL Configuration
GRAPHENE = {
    'SCHEMA': 'salalem_project.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
}    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
### ✅ urls.py
```python
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt  # Required
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    # csrf_exempt is REQUIRED for React to access GraphQL
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
```


## 🛠️ Run Migrations
python manage.py migrate

## ▶️ Run the Server
python manage.py runserver

### Example Queries
we will follow this formatt
first query name then query formatt between ======
### Artists
get all Artists with albums (relationship) them get the songs name that linked with album
==============================================
query allArtists{
  allArtists{

id,name,birthYea,albums{
      title,songs{
        title
      }
    }
  }
}

================================================
get one Artisit by id
==============================================
query getArtist{
  artistById(id:1){
    name,id,bio,birthYear,albums{
      title,
      songs{
        title,duration
      }
    }
  }
}

================================================
add new Artist
========================================================
mutation AddNewArtist {
  createArtist(name:"test", bio: "test abc", birthYear: 2020) {
    artist {
      id
      name
      bio
      birthYear
    }
  }
}
================================================
### Songs
get all songs with ahbum (relationships)
==============================================
query allSongs{
  allSongs{
    id,title,duration,trackNumber,album{
      title,artist{
        name
      }
    }
  }
}
==============================================
### Albums
get all Albums with songs and Artist (relationships)
==============================================
query allAlbums{
  allAlbums{
    id,title,releaseDate,songs{
      title
    },artist{
      name
    }
  }
}
==============================================
