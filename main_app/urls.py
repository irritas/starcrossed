from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('users/', views.users_index, name='users_index'),
	path('users/<user_id>/', views.users_detail, name='users_detail'),
    path('signs/', views.signs_index, name='signs_index'),
    path('signs/<sign_name>/', views.signs_detail, name='signs_detail'),
    path('users/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
]