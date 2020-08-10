from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Images(models.Model):
    ''' a model for Image posts '''
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True)
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['?'] #order randomly on feed


class Profile(models.Model):
    ''' a User model extended'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hi, my name is {User.username}')

    def __str__(self):
        return f'user {self.user.username}'
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Comments(models.Model):
    ''' a model for comments'''
    # related_post = models.ForeignKey('Images', on_delete=models.CASCADE)
    name = models.ForeignKey('Profile', on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment by {self.name}'



class Relations(models.Model):
    follower = models.ForeignKey('Profile', related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey('Profile', related_name='followers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'followed')

    def __str__(self):
        return '{self.follower} follows {self.followed}'