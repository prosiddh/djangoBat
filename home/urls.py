from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("service/",views.service,name='service'),
    path("help/",views.help,name='help'),
    path("contact/",views.contact,name='contact')
]
