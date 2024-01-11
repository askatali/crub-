from django.urls import path
from product.views import product_list, product_detail

urlpatterns = [
    path('list/', product_list, name='list'),
    path('detail/<int:pk>/', product_detail, name='detail')
]
