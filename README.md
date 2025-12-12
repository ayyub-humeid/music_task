
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
### 3. Install dependencies
pip install -r requirements.txt

## 🛠️ Run Migrations
python manage.py migrate

## ▶️ Run the Server
python manage.py runserver

### Example Queries
we will follow this formatt
first query name then query formatt between ======
### Artists
get all Artists
==============================================
query allArtists{
  allArtists{
    name,albums{
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
