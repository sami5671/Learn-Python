from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path("student/", include("student.urls")),
    path("teacher/", include("teacher.urls")),
]
