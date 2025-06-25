from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def profile(request):
    return HttpResponse("Student profile")


def home(request):
    user_data = {"name": "abdur rahim", "age": 200, "married": True}
    return render(request, "student/index.html", user_data)
