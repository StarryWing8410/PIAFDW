from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'principal.html')

def cajas(request):
    return render(request,'cajas.html')

def estanteria(request):
    return render(request,'estanteria.html')

def lockers(request):
    return render(request,'lockers.html')

def muebles(request):
    return render(request,'muebles.html')

def admin(request):
    return render(request,'admin.py')