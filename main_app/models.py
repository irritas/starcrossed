from django.db import models
from django.contrib.auth.models import User
import requests

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

SIGNS = (
	'Aries',
	'Taurus',
	'Gemini', 
	'Cancer',
	'Leo',
	'Virgo',
	'Libra',
	'Scorpio',
	'Sagittarius',
	'Capricorn',
	'Aquarius',
	'Pisces'
)

SIGNS_LOOKUP = {
	'Aries' : 'Ram',
	'Taurus' : 'Bull',
	'Gemini' : 'Twins',
	'Cancer' : 'Crab',
	'Leo' : 'Lion',
	'Virgo' : 'Maiden',
	'Libra' : 'Scales',
	'Scorpio' : 'Scorpion',
	'Sagittarius' : 'Archer',
	'Capricorn' : 'Goat',
	'Aquarius' : 'Water-bearer',
	'Pisces' : 'Fish'
}

class Sign(models.Model):
	name = models.CharField(
		max_length=20,
		choices=SIGNS,
	)
	sign_api = requests.get(f'https://zodiacal.herokuapp.com/{name}').json()