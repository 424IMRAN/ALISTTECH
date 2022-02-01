import requests
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return  render(request,'base.html')
def about(request):
    return render(request,'pages/about-us.html')
def contact(request):
    return render(request,'pages/contact-us.html')