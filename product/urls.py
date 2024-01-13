from django.urls import path

from product.views import ProductListView, product_detail

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', product_detail, name='detail')
]
