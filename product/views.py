from django.shortcuts import render
from .models import scents, colours


def shop_product(request):
    """ A view to show the product options """

    Scent = scents.objects.all()
    Colour = colours.objects.all()

    context = {
        'Scent': Scent,
        'Colour': Colour,

    }

    return render(request, 'product/products.html', context)
