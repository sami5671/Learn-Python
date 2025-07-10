from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post, Tag


# Create your views here.
def post_list(request):
    # category, tag, searching, pagination
    categoryQ = request.GET.get("category")
    tagQ = request.GET.get("tag")
    searchQ = request.GET.get("q")

    posts = Post.objects.all()

    if categoryQ:
        posts = posts.filter(category__name=categoryQ)
    if tagQ:
        posts = posts.filter(tag__name=tagQ)
    if searchQ:
        posts = posts.filter(
            Q(title__icontains=searchQ)
            | Q(content__icontains=searchQ)
            | Q(category__name__icontains=searchQ)
            | Q(tag__name__icontains=searchQ)
        ).distinct()

    # pagination
    paginator = Paginator(posts, 2)  # per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "search_query": searchQ,
        "category_query": categoryQ,
        "tag_query": tagQ,
    }
    return render(request, "", context)
