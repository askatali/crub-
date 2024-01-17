from django.shortcuts import render
from product.models import Product
from django.views.generic import TemplateView


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

