from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request,'contact.html')

def readmore(request):
    return render(request, 'readmore.html')
