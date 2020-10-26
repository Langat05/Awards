
from django.test import TestCase



# Create your tests here.

class ProfileTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('langat')
        cls.profile1 = Profile(profile_pics = 'bab.jpg', bio = 'born in Kenya', user = cls.user)

    def test_instance(cls):
        cls.assertTrue(isinstance(cls.profile1, Profile))

    def save_method_test(self):
        self.profile1.save_profile()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)    

class ImageTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user('langat')
        cls.new_profile = Profile(profile_pics = 'bab.jpg', bio = 'born in Kenya', user = cls.user)
        cls.new_image = Image(my_image='/static/images/', caption='Corona', profile=cls.new_profile)

    def test_instance_true(cls):
        cls.assertTrue(isinstance(cls.new_image, Image))

    def test_save_image_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()        