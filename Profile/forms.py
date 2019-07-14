from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30 , required=False)    
    blood_group = forms.CharField(max_length=1,required=True)
    email = forms.EmailField(max_length=254)
    address =forms.CharField(max_length=100)
    city =forms.CharField(max_length =100)
    about_me =forms.CharField(max_length=1000)
    

    class meta:
        model =User
        fields =('name','email','blood_group','address','city','password2','about_me')



class donateForm(forms.ModelForm):
    email = forms.EmailField(max_length = 254 ,required =False)
    
    
    class Meta:
        model = Person
        fields =('email','address','blood_grp','phone')
