from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=12)
    email = forms.CharField(max_length=40)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "name", "surname", "phone_number", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(NewUserForm, self.save(commit=False))
