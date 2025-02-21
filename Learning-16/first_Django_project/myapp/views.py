from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Hello, Welcome to Django!")


def info(request):
    return HttpResponse("Welcome to Info page!")
