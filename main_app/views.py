from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from datetime import date
import requests

def home(request):
    return redirect('signs_index')

def signup(request):
	error_message = ''
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.name = form.cleaned_data.get('name')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			month = user.profile.birth_date.month
			day = user.profile.birth_date.day
			if month == 1:
				if day > 20: user.profile.sign = 'Aquarius'
				else: user.profile.sign = 'Capricorn'
			if month == 2:
				if day > 19: user.profile.sign = 'Pisces'
				else: user.profile.sign = 'Aquarius'
			if month == 3:
				if day > 20: user.profile.sign = 'Aries'
				else: user.profile.sign = 'Pisces'
			if month == 4:
				if day > 20: user.profile.sign = 'Taurus'
				else: user.profile.sign = 'Aries'
			if month == 5:
				if day > 20: user.profile.sign = 'Gemini'
				else: user.profile.sign = 'Taurus'
			if month == 6:
				if day > 21: user.profile.sign = 'Cancer'
				else: user.profile.sign = 'Gemini'
			if month == 7:
				if day > 22: user.profile.sign = 'Leo'
				else: user.profile.sign = 'Cancer'
			if month == 8:
				if day > 23: user.profile.sign = 'Virgo'
				else: user.profile.sign = 'Leo'
			if month == 9:
				if day > 21: user.profile.sign = 'Libra'
				else: user.profile.sign = 'Virgo'
			if month == 10:
				if day > 22: user.profile.sign = 'Scorpio'
				else: user.profile.sign = 'Libra'
			if month == 11:
				if day > 21: user.profile.sign = 'Sagittarius'
				else: user.profile.sign = 'Scorpio'
			if month == 12:
				if day > 21: user.profile.sign = 'Capricorn'
				else: user.profile.sign = 'Sagittarius'
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('home')
		else:
			error_message = form.errors
	form = SignUpForm()
	context = {'form': form, 'error_message': error_message}
	return render(request, 'registration/signup.html', context)

# @login_required
# def user_index(request):
#     users = User.objects.all()
#     return render(request, 'user/index.html', { 'users': users })

#Sarah's codes
# def user_detail(request, user_id):
#   user = User.objects.get(id=user_id)
#   return render(request, 'main_app/user_detail.html', {'user': user})

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