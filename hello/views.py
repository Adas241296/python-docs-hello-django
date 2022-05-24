from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello Amdocs Team - Good morning, we are all happy")
