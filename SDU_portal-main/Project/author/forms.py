from fileinput import FileInput
from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms import ImageField, ModelForm, TextInput, Textarea
from django.contrib.auth.models import User

# from Project import author
from .models import Blogs, Category,Comment, ProfileInfo
from django.core.exceptions import ValidationError

from .models import *



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeHolder': 'Login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeHolder': 'Password'}))

choices = Category.objects.all().values_list('name','name')

choices_list = []
for item in choices:
    choices_list.append(item)

class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blogs
        fields = ('title','img_url','description','category')

        widgets = {
            'title': forms.TextInput(),
            'img_url': forms.FileInput(),
            'description': forms.Textarea(),
            'category':forms.Select(choices=choices_list)
        }
    def create_obj(self, something):
        title = self.cleaned_data['title']
        img_url = self.cleaned_data['img_url']
        description = self.cleaned_data['description']
        category = self.cleaned_data['category']
        Blogs.objects.create(title=title, img_url=img_url, description=description, author_id=something, category=category)
        

            
class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('body',)
        widget = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeHolder': 'Write Comment'}),
        }

        
class NewUserForm(UserCreationForm):
    email= forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username" , "email" , "password1" , "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
            return user

def __init__(self, *args, **kwargs):
    super(NewUserForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['class'] = 'form-control'



class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
  

    class Meta:
        model = ProfileInfo
        fields = '__all__'
        exclude = ['user']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)