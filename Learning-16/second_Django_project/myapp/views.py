from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homePage(request):
    return HttpResponse("Welcome to django Home page")


def aboutPage(request):
    return HttpResponse("Welcome to django About page")


def contactPage(request):
    return HttpResponse("Welcome to django Contact page")
