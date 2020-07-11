from django.urls import path
<<<<<<< HEAD
from Fit.views import HomeView, RegisterView, SuccessView


urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('success/', SuccessView.as_view(), name = 'success'),
=======
from Fit import views

urlpatterns = [
    path('', views.home, name = 'home'),
>>>>>>> 2a4df85ffcf0939797e836593b28770b612d931d
]
