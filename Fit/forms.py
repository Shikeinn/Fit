from django import forms
from Fit.models import User

sex = (('male', 'male'), ('female', 'female'))

class UserForm(forms.Form):
    heightFeet = forms.IntegerField(label='Height:', min_value=0, max_value=12)
    heightInches = forms.IntegerField(label='', min_value=0, max_value=11)
    weight = forms.IntegerField(label='Weight:', min_value=0)
    age = forms.IntegerField(label='Age:', min_value=0, max_value=100)
    sex = forms.ChoiceField(label='Gender:', choices = sex)