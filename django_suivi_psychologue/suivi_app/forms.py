from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from suivi_app.models import User
# from suivi_app.widget import DateTimePickerInput
from django.forms import widgets


# Formulaire de connexion
class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    

# Formulaire d'inscription 
class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')


# Formulaire de mofification du compte
class ModifCompte(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username','email', 'first_name', 'last_name',)

