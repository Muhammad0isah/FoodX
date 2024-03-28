from django.db import models
from django.conf import settings


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    image_url = models.ImageField(upload_to='static/event-image')

    def __str__(self):
        return self.name

