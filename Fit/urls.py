from django.urls import path
from Fit.views import RegisterView, SuccessView
from Fit import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('success/', SuccessView.as_view(), name = 'success'),
]