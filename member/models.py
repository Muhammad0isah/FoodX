from django.db import models


# Create your models here

class ISADMembers(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.ImageField(upload_to='static/member-images',null=True,blank=True)