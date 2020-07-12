from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Fit.models import UserInfo
from Fit.forms import UserForm

# Create your views here.

@login_required
def home(request):
    args = {}
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if (form.is_valid()):
            userInfo = UserInfo()
            userInfo.user = request.user
            userInfo.weight = request.POST.get('weight')
            userInfo.height = (request.POST.get('heightFeet') * 12) + request.POST.get('heightInches')
            userInfo.gender = request.POST.get('gender')
            userInfo.save()
        
        return render(request, 'home.html', args)

        
    else:
        try:
            userInfo = UserInfo.objects.get(user=request.user)
        except UserInfo.DoesNotExist:
            userInfo = None
            form = UserForm()
        args = {
            'userInfo': userInfo,  
            'form': form,      
        }
        return render(request, 'home.html', args)

    
    
    

class HomeView(TemplateView):
    template_name = "home.html"
    
class SuccessView(TemplateView):
    template_name = "registration/success.html"

class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def get(self, request):
        form = UserCreationForm()
        args = {'form':form}
        return render(request, self.template_name, args)

    def post(self, request):
        #if request.method == 'POST':
        form = UserCreationForm(request.POST)
        args = {'form':form}
        print(form.is_valid())
        print(form.errors)
        if (form.is_valid()):
            form.save()
            return redirect("/success")

        # else:
        #     print(form.errors)
        #     form = UserCreationForm()
        return render(request, self.template_name, args)

    # def get(self, request):
    #     form = UserForm() #initialize form
    #     args = {'form': form}
    #     User.objects.all().delete() #clears data from last session
    #     return render(request, self.template_name, args)
    # def post(self, request):
    #     form = UserForm(request.POST) #grabs form from POST request
    #     if (form.is_valid()):
    #         first_name = form.cleaned_data['first_name'] #cleaned_data gives SQL injection protection
    #         last_name = form.cleaned_data['last_name']
    #         p = User(first_name = first_name, last_name = last_name ) #create newe User object
    #         p.save() #push new object to User model
    #         name_list = User.objects.all() #pulls all data from the User model
    #         args = {'form': form, 'first_name':first_name, 'last_name':last_name, 'list':name_list}
    #     return render(request, self.template_name, args)

# Create your views here.

class HomeView(TemplateView):
    template_name="base.html"
    def get(self, request):
        args ={'test':'asdf'}
        print('asdf')
        return render(request, self.template_name)

def hello(request):
    print("HIT IN PYTHON")
    return HttpResponse('Hello World')
