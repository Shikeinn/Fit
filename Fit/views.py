from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from Fit.models import User
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    def get(self, request):
        bruh = "Hello World #swagmoney #cashhaver #dollarowner"
        user = User.objects.all()
        args = {'user': user}
        return render(request, self.template_name, args)