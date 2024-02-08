from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from next.serializers import EmailSerializer
from rest_framework.response import Response
from rest_framework import status


class EmailCreateView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = EmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Method 1
        serializer.save(password=39)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
