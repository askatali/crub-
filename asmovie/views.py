from django.shortcuts import render
from asmovie.models import Movie
from asmovie.pagination import MoviePagination
from asmovie.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import UpdateAPIView



class MovieList(GenericAPIView):
    permission_classes = (AllowAny,)
    pagination_class = MoviePagination
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get(self, request):
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data  # pagination data
        else:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            data = serializer.data
        return Response(data)


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
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        

class MovieUpdateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
