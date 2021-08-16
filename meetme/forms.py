from django import forms
#from .models import Participants

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length= 50, label='Your Name')
    email = forms.EmailField(label = "Your Email")
    