from django.urls import path

from product.views import product_list

urlpatterns = [
    path('index/', product_list, name='index')
]
