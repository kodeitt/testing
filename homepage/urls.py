from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('index',views.index),
    path('login', views.login),
    path('contact',views.contact),
    path('readmore',views.readmore),
    path('Dashboard',views.Dashboard),
    path('/static/service.html', views.service)
    
    

]