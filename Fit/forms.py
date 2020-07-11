from django import forms
from models import User

class UserForm(forms.Form):
    first_name = forms.CharField(label="first name:")
    last_name = forms.CharField(label="last name:")