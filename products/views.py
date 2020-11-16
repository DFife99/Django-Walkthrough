from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ a view to return all_products.html, including sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
