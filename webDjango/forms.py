from django import forms

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