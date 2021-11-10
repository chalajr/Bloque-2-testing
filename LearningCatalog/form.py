from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, forms
from accounts.models import *


class Search(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)
