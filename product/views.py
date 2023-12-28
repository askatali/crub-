from django.shortcuts import render
from product.models import Product


def product_list(request):
    products = Product.objects.order_by('-size')
    return render(request,
                  'index.html',
                  context={'products': products}
                  )
