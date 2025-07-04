from django.urls import path

from . import views

urlpatterns = [
    path("one-to-one/", views.demo_one_to_one, name="one-to-one"),
    path("user/<int:pk>", views.user, name="user"),
    path("one-to-many/", views.demo_one_to_many, name="one-to-many"),
]
