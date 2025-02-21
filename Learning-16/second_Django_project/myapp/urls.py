from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.homePage, name="home"),
    path("about/", views.aboutPage, name="about"),
    path("contact/", views.contactPage, name="contact"),
]
