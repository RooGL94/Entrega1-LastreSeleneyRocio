from django import forms
from products.models import cositas 
from products.models import ofertas
from products.models import segunda_mano

class product_form(forms.ModelForm):
    class Meta:
        model = cositas
        fields = '__all__'

class product_form(forms.ModelForm):
    class Meta:
        model = ofertas
        fields = '__all__'

class product_form(forms.ModelForm):
    class Meta:
        model = segunda_mano
        fields = '__all__'



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}