from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("create/", views.create_student, name="create_student"),
]
