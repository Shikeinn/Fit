from django.urls import path
from Fit.views import HomeView, RegisterView, SuccessView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('success/', SuccessView.as_view(), name = 'success'),
]
