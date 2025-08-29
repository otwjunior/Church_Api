"""
URL configuration for church_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Church Media API 🎶</h1><p>Welcome! Use the endpoints below:</p><ul><li>/api/songs/</li><li>/api/users/</li></ul>")

urlpatterns = [
    path('', home, name='home'), #simple homepage
    path('admin/', admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/songs/", include("songs.urls")),
    path("api/sermons/", include("sermons.urls")),
]
