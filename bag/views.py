from django.shortcuts import render, redirect
from .models import Cart


def view_bag(request):
    """ A view that renders the bag contents page """
    cart = Cart.objects.all()
    context = {
        'cart': cart,
    }

    return render(request, 'bag/bag.html', context)
