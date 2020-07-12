from django import forms
from Fit.models import User

sex = (('male', 'male'), ('female', 'female'))

class UserForm(forms.Form):
    heightFeet = forms.IntegerField(min_value=0, max_value=12)
    heightInches = forms.IntegerField(min_value=0, max_value=11)
    weight = forms.IntegerField(min_value=0)
    age = forms.IntegerField(min_value=0, max_value=100)
    sex = forms.ChoiceField(choices = sex)