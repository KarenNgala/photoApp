from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)



class Profile(models.Model):
    photo = models.ImageField(upload_to='avatars/')
    bio = models.TextField()