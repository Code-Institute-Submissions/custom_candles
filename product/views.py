from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import scents, products


def all_products(request):
    """ A view to show the list of products """

    product = products.objects.all()

    context = {
        
        'product': product,
    }

    return render(request, 'product/products.html', context)


def product_detail(request, products_id):
    """ A view to show individual product details """

    product_det = get_object_or_404(products, pk=products_id)
    scent = scents.objects.all()

    context = {
        'product_det': product_det,
        'scent': scent,
    }

    return render(request, 'product/product_detail.html', context)

