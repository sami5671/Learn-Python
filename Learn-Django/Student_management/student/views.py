from django.http import HttpResponse
from django.shortcuts import redirect, render

from . import forms, models
from .forms import StudentForm

# Create your views here.

# 1. HTML form
# 2. Form Api
# 3. Model Form


# def home(request):
# print(request.POST)
# this for HTML form
# if request.method == "POST":
#     name = request.POST.get("name")
#     email = request.POST.get("email")
#     phone = request.POST.get("phone")
#     password = request.POST.get("password")
#     checkbox = request.POST.get("checkbox")
#     photo = request.FILES.get("photo")

#     if checkbox == "on":
#         checkbox = True
#     else:
#         checkbox = False

#     student = models.Student(
#         name=name,
#         email=email,
#         phone=phone,
#         password=password,
#         checkbox=checkbox,
#         photo=photo,
#     )  # student class er akta object
#     student.save()
#     return render(request, "student/index.html")
# else:
#     return render(request, "student/index.html")

# this for model form


def create_student(request):
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.StudentForm()
    return render(request, "student/create_student.html", {"form": form})


def home(request):
    students = models.Student.objects.all()
    return render(request, "student/index.html", {"students": students})
