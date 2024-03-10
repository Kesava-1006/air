from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from .models import *
# Create your views here.
def loginfun(request):
    return render(request, "login.html")
def signup(request):
    return render(request,"signup.html")

def home(request):
    return render(request,"home.html")

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Register


def regfun(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password=request.POST.get('password')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered. Choose a different email.")
        Register.objects.create(username=username,  email=email,password=password)
        return render(request, 'login.html')
    return render(request,'login.html')

def loginfun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        if Register.objects.filter(username=username,password=pass1).exists():
            return redirect('home')
        else:
            return HttpResponse("Username And Password is Incorrect")

    return render(request, 'login.html')

def flight_list(request):
    flights = Flight.objects.all()  # Retrieve all flights from the database
    return render(request, 'flight.html', {'flights': flights})
def payment(request):
    return render(request,'payment.html')
def about(request):
    return render(request,'about.html')