from django.shortcuts import render
# from .models import {the database name}  #create the database in models.py under homepage section
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request,'contact.html')

def readmore(request):
    return render(request, 'readmore.html')



def service(request):
    return render(request, 'service.html')

def Dashboard(request):
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    data={database_name}.objects.filter(Q(case_id__icontains=q)|Q(lawyer_name__icontains=q))
    return render(request, 'dashboard.html',{'data':data})



    


