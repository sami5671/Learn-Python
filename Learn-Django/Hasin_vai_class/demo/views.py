from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    person = {
        "name": "jhone",
        "age": 30,
        "hobbies": ["cinema", "sports", "pets"],
        "gender": "Male",
    }
    location = "Dhaka"
    return render(
        request, "index.html", context={"location": location, "person": person}
    )
