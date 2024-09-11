from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm 

def home_view(request):
    return render(request, 'base.html')

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ya puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de login después del registro exitoso
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

# Vista para el inicio de sesión de usuarios
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


# @login_required
# def profile_view(request):
#     user = request.user
#     return render(request, 'users/profile.html', {'user': user})

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/profile_edit.html', {'form': form})
