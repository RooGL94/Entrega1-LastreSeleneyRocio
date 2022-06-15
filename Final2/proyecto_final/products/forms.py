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