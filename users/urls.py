# users/urls.py

from django.urls import path
from movies.views import movie_list

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('formulario/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('api/logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profiles/', views.profile_list, name='profile_list'),  # Lista de perfiles disponibles

    path('profile/add/', views.profile_add, name='profile_add'),
    path('profile/select/', views.select_profile, name='select_profile'),


    path('movies/<int:profile_id>/', movie_list, name='movie_list'),

  
]


