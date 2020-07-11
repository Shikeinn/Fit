from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Fit.forms import UserForm
from Fit.models import User
from Fit.forms import UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

class HomeView(TemplateView):
    template_name="base.html"
    def get(self, request):
        args ={'test':'asdf'}
        print('asdf')
        return render(request, self.template_name)

def hello(request):
    return HttpResponse('Hello World')