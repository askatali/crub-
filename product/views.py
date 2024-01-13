from django.shortcuts import render
from product.models import Product
from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        products = Product.objects.order_by('-size')
        return {'products': products}


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
