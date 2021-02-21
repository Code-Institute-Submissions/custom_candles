from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import scents, products


def all_products(request):
    """ A view to show the list of products """

    scent = scents.objects.all()
    product = products.objects.all()

    context = {
        'scent': scent,
        'product': product,
    }

    return render(request, 'product/products.html', context)


def product_detail(request, product_id):
    """ A view to show the detail for the product selected """

    product = get_object_or_404(products, pk=product_id)
    scent = scents.objects.all()

    context = {
        'scent': scent,
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)

