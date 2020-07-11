from django.urls import path
from Fit.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
]
