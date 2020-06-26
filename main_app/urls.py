from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('users/', views.users_index, name='users_index'),
	# path('users/<user_id>/', views.users_detail, name='users_detail'),
	# path('users/<user_id>/bio', views.users_bio, name='users_bio'),
	path('users/<int:user_id>/', views.users_detail, name='users_detail'),
    path('signs/', views.signs_index, name='signs_index'),
    path('signs/<sign_name>/', views.signs_detail, name='signs_detail'),
    path('users/<int:user_id>/add_photo/', views.add_photo, name='add_photo'),
    path('chats/add_chat/<user_a_id>+<user_b_id>/', views.add_chat, name='add_chat'),
	path('chats/<int:chat_id>/', views.chats_detail, name='chats_detail'),
]