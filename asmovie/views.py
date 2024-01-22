from django.shortcuts import render
from asmovie.models import Movie
from django.views.generic import TemplateView
from asmovie.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class MovieList(APIView):
    permission_classes = (AllowAny,)

    def get(request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetail(APIView):
    permission_classes = (AllowAny,)

    def get(request, *args, **kwargs):
        print(Movie.objects.all())
        products = Movie.objects.get(id=kwargs.get('id'))
        serializer = MovieSerializer(products, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

