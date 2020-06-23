from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

def home(request):
    return render(request, 'home.html')

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

@login_required
def user_index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', { 'users': users })

def signs_detail(request, sign):
	fortune = requests.get(f'http://horoscope-api.herokuapp.com/horoscope/today/{sign}').json()
	return render(request, 'signs/detail.html',	{
		'sign': sign
	})