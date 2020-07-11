from django import forms
from Fit.models import User

class UserForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)