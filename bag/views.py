from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .models import Cart
from product.models import products


def view_bag(request):
    """ A view that renders the bag contents page """
    cart = Cart.objects.all()
    context = {
        'cart': cart,
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    scent_one = request.POST['scent_one_select']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if scent_one in bag[item_id]['scent_one_dic'].keys():
            bag[item_id]['scent_one_dic'][scent_one] += quantity
        else:
            bag[item_id] = {'scent_one_dic': {scent_one: quantity}}
    else:
        bag[item_id] = {'scent_one_dic': {scent_one: quantity}}

    request.session['bag'] = bag
    return redirect(redirect_url)






