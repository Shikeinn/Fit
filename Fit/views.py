from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Fit.models import User
from Fit.forms import UserForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request):
        form = UserForm() #initialize form
        args = {'form': form}
        User.objects.all().delete() #clears data from last session
        return render(request, self.template_name, args)
    def post(self, request):
        form = UserForm(request.POST) #grabs form from POST request
        if (form.is_valid()):
            first_name = form.cleaned_data['first_name'] #cleaned_data gives SQL injection protection
            last_name = form.cleaned_data['last_name']
            p = User(first_name = first_name, last_name = last_name ) #create newe User object
            p.save() #push new object to User model
            name_list = User.objects.all() #pulls all data from the User model
            args = {'form': form, 'first_name':first_name, 'last_name':last_name, 'list':name_list}
        return render(request, self.template_name, args)