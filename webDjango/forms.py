from django import forms

class Registro(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=25)
    correo = forms.EmailField(required=True)
    password = forms.CharField(required=True)