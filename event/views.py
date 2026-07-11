from django.shortcuts import render
from django.http import HttpResponse
# from event.forms import . 
# Create your views here.

def home(request):
    return render(request,'Dashbord.html')

def addCategory(request):
    
    pass  