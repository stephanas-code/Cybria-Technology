from django.contrib.auth.models import User
from django import forms
from .models import *
from django import forms  
from django.contrib.auth.forms import UserCreationForm  

from django.forms.forms import Form  



class BecomeadeveloperForm(forms.ModelForm):
    class Meta:
        model = Becomeadeveloper
        fields = ['firstname', 'lastname','email' ,'phone','skills']  



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'subject','email' ,'message'] 