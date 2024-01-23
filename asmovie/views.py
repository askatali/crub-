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
        movie = Movie.objects.get(id=kwargs.get('id'))
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieCreateView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = MovieSerializer

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Method 1
        serializer.save(movie_age=39)

        # Method 2
        # Movie.objects.create(**serializer.validated_data, movie_age=39)

        # Method 3
        # Movie.objects.create(
        #     name=serializer.validated_data['name'],
        #     country=serializer.validated_data['country'],
        #     production_year=serializer.validated_data['production_year'],
        #     movie_age=serializer.validated_data['movie_age'],
        #     time=serializer.validated_data['time'],
        #     genre=serializer.validated_data['genre']
        # )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
