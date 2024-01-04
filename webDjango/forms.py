from django import forms
from django.contrib.auth.models import User

class Registro(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=25,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Usuario'}))
    correo = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Correo'
    }))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))

    password2 = forms.CharField(required=True,label='Confirmar contraseña', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirmar contraseña'

    }))
    def clean_username(self):
        username = self.cleaned_data.get('username')
    
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya creado ')
    
        return username
    
    def clean_email(self):
        correo = self.cleaned_data.get('correo')

        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('Correo ya existe')

        return correo
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','La contraseña es diferente')

    def save(self):
        
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('correo'),
            self.cleaned_data.get('password')
            )
        return user
        
