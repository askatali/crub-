from django.urls import path

from product.views import product_list

urlpatterns = [
    path('list/', product_list, name='index'),
]
