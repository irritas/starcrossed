from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    # path('accounts/index/', views.user_index),
    path('signs/', views.signs_index, name='signs_index'),
    path('signs/<sign_name>/', views.signs_detail, name='signs_detail'),
]