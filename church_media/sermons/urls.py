from django.urls import path
from .views import SermonListCreateView, SermonDetailView

urlpatterns = [
    path("", SermonListCreateView.as_view(), name="sermon-list-create"),
    path("<int:pk>/", SermonDetailView.as_view(), name="sermon-detail"),
]
