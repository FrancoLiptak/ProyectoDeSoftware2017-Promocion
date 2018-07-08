from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):

    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'group',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',            
            'group': 'Tipo de usuario',            
        }

class UpdateUserForm(UserCreationForm):

    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'group',
            'is_active',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',            
            'group': 'Tipo de usuario',
            'is_active': 'Usuario Activo (no bloqueado)',
        }