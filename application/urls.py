from django.urls import path
from .views import *


urlpatterns = [
    path('login', loginfun, name='login'),
    path('signup', signup, name='signup'),
    path('', home, name='home'),
    path('register', regfun, name="register"),
    path('flights',flight_list, name='flight_list'),
    path('payment',payment,name='payment'),
    path('about',about,name='about'),
]
