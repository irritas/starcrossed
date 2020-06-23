from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/index/', views.user_index),
    path('signs/<sign>/', views.signs_detail, name='detail'),
]