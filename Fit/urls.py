from django.urls import path
from Fit import views

urlpatterns = [
    path('', views.home, name = 'home'),
]
