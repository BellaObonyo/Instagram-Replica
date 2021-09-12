from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Comment,Image
from django.contrib.auth.models import User

class postPhotoForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ['photo','photo_name','photo_caption']

class CommentsForm(forms.ModelForm):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['comment'].widget=forms.TextInput()
    self.fields['comment'].widget.attrs['placeholder']='Leave a comment...'
  class Meta:
    model = Comment
    fields = ('comment',)
    
class Registration(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_photo','bio']

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']





