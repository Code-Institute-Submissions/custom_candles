from django.shortcuts import render, redirect
from product.models import scents, products

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def view_scents(request):
    """ A view to return the index page """
    scent = scents.objects.all()

    context = {
        'scent': scent,
    }

    return render(request, 'home/scents.html', context)