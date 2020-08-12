from django.test import TestCase
from .models import Images, Profile, Comments, Relations
from datetime import datetime
from django.contrib.auth.models import User


class TestImages(TestCase):
    ''' test class for images model '''
    def setUp(self):
        ''' method to create Image instances to be called before each test case'''
        self.test_user = User(username='Linda', password='123')
        self.test_user.save()
        self.test_profile = Profile(user=self.test_user, photo='avatars/anime.jpg')

        self.test_comment = Comments(name=self.test_profile, comment_body='Test comment', created_on=datetime.now())

        self.test_image = Images(image='images/test.jpg', caption='some text', profile=self.test_profile, comments=self.test_comment, created_on=datetime.now())

    def test_instance(self):
        ''' '''
        self.assertTrue(isinstance(self.test_image, Images))

    def tearDown(self):
        ''' '''
        self.test_user.delete()
        Profile.objects.all().delete()
        Comments.objects.all().delete()
        Images.objects.all().delete()