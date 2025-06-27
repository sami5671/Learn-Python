from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.


def home(request):
    # print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        checkbox = request.POST.get("checkbox")
        photo = request.FILES.get("photo")

        if checkbox == "on":
            checkbox = True
        else:
            checkbox = False

        student = models.Student(
            name=name,
            email=email,
            phone=phone,
            password=password,
            checkbox=checkbox,
            photo=photo,
        )  # student class er akta object
        student.save()
        return render(request, "student/index.html")
    else:
        return render(request, "student/index.html")
