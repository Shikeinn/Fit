from django.urls import path
from Fit import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name = 'home')
    , url(r'^hello/', views.hello, name='hello')
]

