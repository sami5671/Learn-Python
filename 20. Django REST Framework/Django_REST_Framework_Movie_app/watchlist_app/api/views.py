from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app import models

from . import serializers


@api_view()
def movie_list(request):
    movies = models.MovieList.objects.all()  # python objects
    serializer = serializers.MovieListSerializer(
        movies, many=True
    )  # python object ot json convert
    return Response(serializer.data)
