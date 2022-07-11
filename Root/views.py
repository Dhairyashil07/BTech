from django.shortcuts import render
from django.http import *
def home(request):
    return render(request,'index.html')
    #render function used to fetch data
    # render static and dynamic data 
def log(request):
    return render(request,"Login_main.html")
# Create your views here.
def conn(request):
    return render(request,"contact.html")

