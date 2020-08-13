from django.test import TestCase
from .models import Image, Profile, Comment, Relation
from datetime import datetime
from django.contrib.auth.models import User



class ProfileTest(TestCase):
    ''' test class for Profile model'''
    def setUp(self):
        self.user = User.objects.create_user(username='Water')

    def tearDown(self):
        self.user.delete()

    def test_profile_creation(self):
        self.assertIsInstance(self.user.profile, Profile)
        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)


class TestImage(TestCase):
    ''' test class for image model '''
    def setUp(self):
        ''' method to create Image instances to be called before each test case'''
        self.test_user = User(username='Linda', password='123')
        self.test_user.save()
        self.test_profile = User.objects.last().profile
        self.test_profile.save()

        self.test_comment = Comment(name=self.test_profile, comment_body='Test comment', created_on=datetime.now())
        self.test_comment.save()

        self.test_image = Image(image='images/test.jpg', caption='some text', profile=self.test_profile, comments=self.test_comment, created_on=datetime.now())

    def test_instance(self):
        ''' test method to ensure image instance creation '''
        self.assertTrue(isinstance(self.test_image, Image))

    def test_save(self):
        ''' test method to save image instance to db '''
        self.test_image.save_image()
        self.assertEqual(len(Image.objects.all()), 1)

    def tearDown(self):
        ''' '''
        self.test_user.delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Image.objects.all().delete()