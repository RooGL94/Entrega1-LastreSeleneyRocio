from django import forms
from products.models import cositas 

class product_form(forms.ModelForm):
    class Meta:
        model = cositas
        fields = '__all__'