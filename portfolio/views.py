
from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    text = {"name":"Abdullah-Al-Fahim",
    'age':23,
    'phone':'01952670178',
    'friend_list':['Polash','Masud','Fahad','Fahim']
    }
    return render (request,'index.html',text)


def about(request):
    return render (request,'about.html')


def contact(request):
    return render (request,'contact.html')

    



