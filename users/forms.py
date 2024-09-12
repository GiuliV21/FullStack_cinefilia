from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from .models import UserProfile


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture', 'bio']




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture', 'bio']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_name', 'profile_picture', 'bio']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def clean(self):
        cleaned_data = super().clean()
        if self.user and UserProfile.objects.filter(user=self.user).count() >= 3:
            raise forms.ValidationError("No puedes tener más de 3 perfiles.")
        
        return cleaned_data