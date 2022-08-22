from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def employee(request):
    return HttpResponse("This is employee Home Page")


def profile(request):
    return render(request, 'employee/profile.html')


def contact(request):
    return HttpResponse("This is Contact Page")