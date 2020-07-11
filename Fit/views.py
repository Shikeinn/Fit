from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Fit.forms import UserForm
from Fit.models import User
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request):
        form = UserForm()
        args = {'form': form}
        return render(request, self.template_name, args)
    def post(self, request):
        if (form.is_valid()):
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            args = {'first_name':first_name, 'last_name':last_name}
        return render(request, self.template_name, args)