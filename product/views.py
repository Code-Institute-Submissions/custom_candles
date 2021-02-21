from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import scents, products


def shop_product(request):
    """ A view to show the product options """

    scent = scents.objects.all()
    product = products.objects.all()
    #product = get_object_or_404(scents, pk=product_id)

    context = {
        'scent': scent,
        'product': product,
        #'product': product,

    }

    return render(request, 'product/products.html', context)
