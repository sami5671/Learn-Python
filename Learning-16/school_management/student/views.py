from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def profile(request):
    return HttpResponse("<h1>Student profile</h1>")


def home(request):
    return HttpResponse("<h1>Student Home</h1>")
