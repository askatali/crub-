from django.urls import path
from product.views import ProductListView, ProductDetailView
from asmovie.views import MovieView

urlpatterns = [
    path('kino/',MovieView.as_view(), name='kino'),

]