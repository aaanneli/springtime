from django import forms
from django.contrib.auth.models import User
from springtime.models import UserProfile

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = UserFormfields = ('username', 'email', 'password')

