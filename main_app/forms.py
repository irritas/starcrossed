from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Chat, Profile
from datetime import date

def check_age(value):
	dob = value
	today = date.today()
	if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
		raise forms.ValidationError('Must be at least 18 years old to register')
	return dob

class SignUpForm(UserCreationForm):
	name = forms.CharField(max_length=30, required=True)
	birth_date = forms.DateField(required=True, validators=[check_age], help_text='Required. Format: YYYY-MM-DD')

	class Meta:
		model = User
		fields = ('username', 'name', 'birth_date', 'password1', 'password2', )

class BioForm(ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', )