from django.db import models

class HeroSection(models.Model):
    image = models.ImageField(upload_to='static/images/hero_images/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserComment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    image = models.ImageField(upload_to='static/member-images',null=True,blank=True)