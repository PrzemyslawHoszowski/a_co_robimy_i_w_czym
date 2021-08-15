from django.http import HttpResponse, response
from django.shortcuts import render
# Create your views here.

def home(response):
    return render(response, "mainsite/home.html", {})

def base(response):
    #return HttpResponse("base")
    return render(response, "mainsite/home.html", {})

def test(request):
    return HttpResponse("kurczaki")