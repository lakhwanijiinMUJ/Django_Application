from django import forms

class RegistrationForms(forms.Form):
    first = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    password = forms.CharField(max_length=120)
    date = forms.DateField()