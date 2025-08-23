
from django.db import models
from django.conf import settings

#sermon models
class Sermon(models.Model):
    title = models.CharField(max_length=255)
    preacher = models.CharField(max_length=255)
    date = models.DateField()
    content= models.TextField()
    category= models.CharField(max_length = 20)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sermons")#user that added the sermon
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.preacher}"
