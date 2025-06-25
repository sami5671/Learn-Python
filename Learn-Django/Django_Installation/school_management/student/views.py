from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def profile(request):
    return HttpResponse("Student profile")


def home(request):
    return render(request, "student/index.html")
