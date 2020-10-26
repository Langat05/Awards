
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