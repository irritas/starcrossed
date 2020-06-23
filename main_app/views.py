from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests, json

def home(request):
    return redirect('signs_index')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# @login_required
# def user_index(request):
#     users = User.objects.all()
#     return render(request, 'user/index.html', { 'users': users })

SIGNS_LOOKUP = {
	'Aries': 'Ram',
	'Taurus': 'Bull',
	'Gemini': 'Twins',
	'Cancer': 'Crab',
	'Leo': 'Lion',
	'Virgo': 'Maiden',
	'Libra': 'Scales',
	'Scorpio': 'Scorpion',
	'Sagittarius': 'Archer',
	'Capricorn': 'Goat',
	'Aquarius': 'Water-bearer',
	'Pisces': 'Fish'
}

def signs_index(request):
	return render(request, 'signs/index.html', {
		'signs': SIGNS_LOOKUP
	})

def signs_detail(request, sign_name):
	sign = requests.get(f'https://zodiacal.herokuapp.com/{sign_name}').json()[0]
	fortune = requests.get(f'https://horoscope-api.herokuapp.com/horoscope/today/{sign_name}').json()
	symbol = SIGNS_LOOKUP[sign_name.capitalize()]
	return render(request, 'signs/detail.html',	{
		'sign': sign,
		'symbol': symbol,
		'fortune': fortune,
		'img_url': f'images/{sign_name}.png'
	})