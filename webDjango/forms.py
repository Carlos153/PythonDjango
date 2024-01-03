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

    def clean_username(self):
        username = self.cleaned_data.get('username')
    
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Usuario ya creado ')
    
        return username
    