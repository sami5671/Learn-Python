from django.urls import path

from . import views

urlpatterns = [
    # path("", views.movie_list),
    # path("<pk>/", views.movie_detail)
    path("", views.MovieListCreateView.as_view()),
    path("<pk>/", views.MovieDetailView.as_view()),
    path("reviews/", views.ReviewListCreateView.as_view(), name="review_list"),
    path("reviews/<pk>/", views.ReviewDetailView.as_view(), name="review_detail"),
]
