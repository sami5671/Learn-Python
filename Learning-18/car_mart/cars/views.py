from django.shortcuts import render

from . import models


# Create your views here.
def home(request):
    car_models = models.CarModel.objects.all()
