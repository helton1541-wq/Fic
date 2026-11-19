from django import forms
from .models import Area, Publico, Curso, Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioCadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nascimento', 'first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nome']

