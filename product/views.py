from product.models import Product
from django.views.generic import TemplateView
from product.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests


class ProductList(APIView):
    permission_classes = (AllowAny,)

    def get(request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetail(APIView):
    permission_classes = (AllowAny,)

    def get(request, *args, **kwargs):
        products = Product.objects.get(id=kwargs.get('id'))
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.order_by('-size')
        return {'products': products}


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        product = Product.objects.get(pk=kwargs.get('pk'))
        return {'product': product}


class ProductCreateView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        Product.objects.create(**serializer.validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)



