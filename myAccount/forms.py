from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from accounts.models import *


class UserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')


class userFormChange(UserChangeForm):
    class Meta:
        model = UserModel
        exclude = '__all__'
        fields = ('first_name', 'last_name',)


class StudentForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('edad',)
