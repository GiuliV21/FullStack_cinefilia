from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm 

def home_view(request):
    return render(request, 'base.html')

# Vista para el registro de usuarios
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ya puedes iniciar sesión.')
#             return redirect('login')  # Redirige a la página de login después del registro exitoso
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'registration/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Tu cuenta ha sido creada, {username}! Ya puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de login después del registro exitoso
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

# Vista para el inicio de sesión de usuarios
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige a la selección de perfiles
        else:
            # Error de autenticación
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')


@login_required
def dashboard_view(request):
    user_profiles = UserProfile.objects.filter(user=request.user)
    return render(request, 'users/dashboard.html', {'user_profiles': user_profiles})

@login_required
def profile_list(request):
    profiles = UserProfile.objects.filter(user=request.user)
    return render(request, 'users/profile_list.html', {'profiles': profiles})



def profile_add(request):
    user = request.user

    # Verificar cuántos perfiles ya tiene el usuario
    existing_profiles_count = UserProfile.objects.filter(user=user).count()
    if existing_profiles_count >= 3:
        messages.error(request, "No puedes tener más de 3 perfiles.")
        return redirect('dashboard')  # Redirige al dashboard si el usuario ya tiene 3 perfiles

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)  # Incluye request.FILES para manejar archivos
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            messages.success(request, "Perfil creado con éxito.")
            return redirect('dashboard')  # Redirige a donde quieras después de crear el perfil
    else:
        form = UserProfileForm()
    
    return render(request, 'users/profile_add.html', {'form': form})


#ver si se usa
# @login_required
# def profile_select(request, profile_id):
#     # Lógica para seleccionar un perfil
#     profile = UserProfile.objects.get(id=profile_id, user=request.user)
#     request.session['selected_profile_id'] = profile.id  # Guardamos el perfil seleccionado en la sesión
#     return redirect('movie_list', profile_id=profile.id)



# def select_profile(request):
#     if request.method == 'POST':
#         # Obtener el 'profile_id' desde los datos POST
#         profile_id = request.POST.get('profile_id')

#         # Verificar si el perfil fue seleccionado
#         if profile_id:
#             # Obtener el perfil seleccionado
#             profile = get_object_or_404(UserProfile, id=profile_id)

#             # Aquí puedes hacer algo con el perfil seleccionado, como almacenarlo en la sesión
#             request.session['selected_profile'] = profile.id

#             # Redirigir a la lista de películas
#             return redirect('movie_list')
    
#     # Si no es POST o no se seleccionó ningún perfil, redirigir a la página de selección de perfiles
#     return redirect('dashboard')
def select_profile(request):
    if request.method == 'POST':
        # Obtener el 'profile_id' desde los datos POST
        profile_id = request.POST.get('profile_id')

        # Verificar si el perfil fue seleccionado
        if profile_id:
            # Obtener el perfil seleccionado
            profile = get_object_or_404(UserProfile, id=profile_id)

            # Aquí puedes hacer algo con el perfil seleccionado, como almacenarlo en la sesión
            request.session['selected_profile'] = profile.id

            # Redirigir a la lista de películas con el profile_id
            return redirect('movie_list', profile_id=profile_id)

    # Si no es POST o no se seleccionó ningún perfil, redirigir a la página de selección de perfiles
    return redirect('dashboard')


# @login_required
# def profile_select(request, profile_id):
#     profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
#     request.session['profile_id'] = profile_id  # Guarda el perfil seleccionado en la sesión
#     return redirect('home')  # O redirige a la página principal o dashboard con contenido



# def some_view(request):
#     profile_id = request.session.get('profile_id')
#     if profile_id:
#         profile = UserProfile.objects.get(id=profile_id)
#         # Usar el perfil seleccionado para mostrar contenido personalizado
#     return render(request, 'some_template.html', {'profile': profile})


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

def logout_view(request):
    logout(request)

    return JsonResponse({'message': 'Logged out successfully'})
