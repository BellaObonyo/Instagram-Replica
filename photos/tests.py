from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image,Profile,Comment

# Create your tests here.
class ProfileTestClass(TestCase):

  def setUp(self):
    self.user = User.objects.create_user("Wendy","pass")
    self.profile_test = Profile(profile_photo='44455444',bio='Scholar',user=self.user)
    self.profile_test.save()

  def test_instance_true(self):
    self.profile_test.save()
    self.assertTrue(isinstance(self.profile_test,Profile))
        
class TestCommentsClass(TestCase):

  def setUp(self):
    self.test_user = User(username = 'Wendy Kinaga')
    self.test_user.save()
    self.photo = Image(photo = 'new_photo.png',photo_name = 'software photo',photo_caption = 'Fitness Coach',user = self.test_user)
    self.comments = Comment(comment = 'Go hard',photo = self.photo,user = self.test_user)

class TestImagesClass(TestCase):

  def setUp(self):

    self.test_user = User(username = 'Barbara')
    self.test_user.save()
    self.photo = Image(photo = 'Barbara.jpeg',name = 'Barbara',caption = 'Barbara',user = self.test_user)
    self.comments = Comment(comment = 'Always Miss Mandi',photo = self.photo,user = self.test_user)

  def test_instance(self):
    self.assertTrue(isinstance(self.photo,Image))

    def test_display_photos(self):
    self.photo.save_photo()
    self.photo2= Image(photo = 'tech.jpeg',name = 'Techitraveller',caption = 'Techi',user = self.test_user)
    self.photo2.save_photo()
    dt = Image.display_photos()
    self.assertEqual(len(dt),2)

  def test_save_photo(self):
    self.photo.save_photo()
    photo = Image.objects.all()
    self.assertTrue(len(photo)>0)

  def test_search(self):
    self.photo.save_photo()
    self.photo2 = Image(photo = 'tech.jpeg',name = 'Techitraveller',caption = 'Techi',user = self.test_user)
    self.photo2.save_photo()
    search_term = "e"
    search1 = Image.search_photos(search_term)
    search2 = Image.objects.filter(name__icontains = search_term)
    self.assertEqual(len(search2),len(search1))

  def test_delete_photo(self):
    self.photo2 = Image(photo = 'tech.jpeg',name = 'Techitraveller',caption = 'Techi',user = self.test_user)
    self.photo2.save_photo()
    self.photo.save_photo()
    self.photo.delete_post()
    photos = Image.objects.all()
    self.assertEqual(len(photos),1)
