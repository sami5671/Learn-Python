from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from .models import Expense, Profile

# Create your views here.


def demo_one_to_one(request):
    profiles = Profile.objects.select_related("user").all()
    # profiles = Profile.objects.select_related("user").filter(location="New York").all()
    # list comprehension
    profile_data = [
        {
            "username": profile.user.username,
            "email": profile.user.email,
            "bio": profile.bio,
            "birth_date": profile.birth_date,
            "location": profile.location,
        }
        for profile in profiles
    ]
    # print(profile_data)
    return JsonResponse(profile_data, safe=False)


def user(request, pk):
    profile = Profile.objects.select_related("user").get(user_id=pk)
    profile_data = {
        "user_id": profile.user_id,
        "username": profile.user.username,
        "email": profile.user.email,
        "bio": profile.bio,
        "birth_date": profile.birth_date,
        "location": profile.location,
    }
    return JsonResponse(profile_data, safe=False)


def demo_one_to_many(request):
    # expenses = Expense.objects.select_related("category").filter(category="1").all()
    # expenses = (
    #     Expense.objects.select_related("category")
    #     .filter(category__name="Transportation")
    #     .all()
    # )
    expenses = (
        Expense.objects.select_related("category").filter(category__name="Food").all()
    )
    # expenses = Expense.objects.select_related("category").all()
    expenses_data = [
        {
            "amount": str(e.amount),
            "category": e.category.name,
            "description": e.description,
        }
        for e in expenses
    ]
    return JsonResponse(expenses_data, safe=False)
