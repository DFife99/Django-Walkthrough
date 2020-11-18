from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ a view to return all_products.html, including sorting and searching """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ a view to return a specific product details """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_detail.html', context)
