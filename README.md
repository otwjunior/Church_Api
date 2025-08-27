# 📖 Church API

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-REST_Framework-red?logo=django)](https://www.django-rest-framework.org/)

A Django REST API for managing church media, including **songs** and **sermons**.  
This project provides a backend solution to help churches store, retrieve, and manage their digital media securely and efficiently.

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
🔑 Authentication

    POST /api/token/ → Obtain JWT token

    POST /api/token/refresh/ → Refresh JWT token

🎵 Songs

    POST /api/songs/ → Create song

    GET /api/songs/ → List songs (supports ?title=, ?category=)

    PATCH /api/songs/{id}/ → Update song

    DELETE /api/songs/{id}/ → Delete song

🎤 Sermons

    POST /api/sermons/ → Create sermon

    GET /api/sermons/ → List sermons

    PATCH /api/sermons/{id}/ → Update sermon

    DELETE /api/sermons/{id}/ → Delete sermon

🧪 Testing

✔️ CRUD operations for songs and sermons tested.
✔️ JWT authentication tested with access & refresh tokens.
✔️ Manual testing performed via Postman/Insomnia.
👨‍💻 Author

James Mwangi
Passionate about backend development, cloud solutions, and building scalable software for Africa.