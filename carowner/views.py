from django.shortcuts import render
from django.http import HttpResponse # type: ignore

# Create your views here.

def sayhello(request):
    return HttpResponse("Hello, world. Welcome.")
