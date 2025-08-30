# 📖 Church API

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-REST_Framework-red?logo=django)](https://www.django-rest-framework.org/)

A Django REST API for managing church media, including **songs** and **sermons**.  
This project provides a backend solution to help churches store, retrieve, and manage their digital media securely and efficiently in a budget friendy way. 

---

## ✨ Features
- 🔑 **JWT Authentication** (login, register, refresh, role-based access).
- 🎵 **Songs Management**
  - Create, list, update, delete songs.
  - Search by **title** or **category**.
- 🎤 **Sermons Management**
  - Create, list, update, delete sermons.
- 👥 **User Roles**
  - Admin & Regular User support.

---

## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** JWT (djangorestframework-simplejwt)  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone <your-repo-url>
cd Church_Api

2️⃣ Create Virtual Environment

python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Database Migration

python manage.py migrate

5️⃣ Run Development Server

python manage.py runserver

📌 API Endpoints
  church-api-862r.onrender.com
🔑 Authentication
  example
  POST church-api-862r.onrender.com/users/register/
  {
    "username": "james",
    "password": "#jamesbark01",
    "email": "james@example.com"
  }

    POST church-api-862r.onrender.com/token/ → Obtain JWT token

    POST church-api-862r.onrender.com/token/refresh/ → Refresh JWT token

🎵 Songs

    POST church-api-862r.onrender.com/songs/ → Create song
    {
    "title": "Jesus Loves Me",
    "artist": "Anna Bartlett Warner",
    "lyrics": "Jesus loves me! This I know, For the Bible tells me so...",
    "category": "Children"
  }

    GET church-api-862r.onrender.com/songs/ → List songs (supports ?title=, ?category=)

    PATCH church-api-862r.onrender.com/songs/{id}/ → Update song

    DELETE church-api-862r.onrender.com/songs/{id}/ → Delete song

🎤 Sermons

    POST church-api-862r.onrender.com/sermons/ → Create sermon
    {
  "title": "Walking in Faith",
  "preacher": "Pastor Td Jakes",
  "date": "2025-08-29",
  "content": "God is not just a father He is a King ...",
  "category": "Kingdom principles"
}
    GET church-api-862r.onrender.com/sermons/ → List sermons

    PATCH church-api-862r.onrender.com/sermons/{id}/ → Update sermon

    DELETE church-api-862r.onrender.com/sermons/{id}/ → Delete sermon

🧪 Testing

✔️ CRUD operations for songs and sermons tested.
✔️ JWT authentication tested with access & refresh tokens.
✔️ Manual testing performed via Postman.

👨‍💻 Author

James Mwangi
Passionate about backend development, cloud solutions, and building scalable software for Africa.
More features to be released soon!!