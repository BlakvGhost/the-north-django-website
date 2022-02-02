from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class InscriptionForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nom', widget=forms.TextInput(attrs={'data-name': 'nom'}))
    last_name = forms.CharField(
        label='Prenom', widget=forms.TextInput(attrs={'data-name': 'nom'}))
    username = forms.CharField(
        label='Nom d\'utilisateur', widget=forms.TextInput(attrs={'data-name': 'nom'}))
    email = forms.CharField(
        label='email', widget=forms.EmailInput(attrs={'data-name': 'email'}))
    password1 = forms.CharField(
        label='password', widget=forms.PasswordInput(attrs={'data-name': 'mdp'}))
    password2 = forms.CharField(
        label='password2', widget=forms.PasswordInput(attrs={'data-name': 'pswd'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
