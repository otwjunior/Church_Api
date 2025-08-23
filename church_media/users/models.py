from django.db import models
from django.contrib.auth.models import AbstractUser

# custom user ith extra fields
class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("media", "Media Team"),
        ("member", "Member"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

