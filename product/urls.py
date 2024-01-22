from django.urls import path
from product.views import ProductListView, ProductDetailView, ProductList, ProductDetail

urlpatterns = [
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('rest_list/', ProductList.as_view(), name='rest_list'),
    path('rest_detail/<int:id>/', ProductDetail.as_view(), name='rest_detail')
]
