from django.shortcuts import render
from .models import scents, colours


def shop_product(request):
    """ A view to show the product options """

    scent = scents.objects.all()
    colour = colours.objects.all()

    context = {
        'scent': scent,
        'colour': colour,

    }

    return render(request, 'product/products.html', context)
