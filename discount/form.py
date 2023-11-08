from django import forms
from .models import appointment

class appointment_form(forms.ModelForm):
    name = forms.CharField(max_length=25)
    service = forms.CharField(max_length=100)
    discount = forms.CharField(max_length=10)
    class Meta :
        model = appointment
        fields = ['name', 'service', 'discount']
        
        