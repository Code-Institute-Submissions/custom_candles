from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from product.models import products




def view_bag(request):
    """ A view that renders the bag contents page """
  


    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    scent_one = request.POST['scent_one_select']
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        if scent_one in bag[item_id]['scent_one_dic'].keys():
            bag[item_id]['scent_one_dic'][scent_one] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = {'scent_one_dic': {scent_one: quantity}}
            messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = {'scent_one_dic': {scent_one: quantity}}
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    scent_one = request.POST['scent_one']
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id]['scent_one_dic'][scent_one] = quantity
    else:
        del bag[item_id]['scent_one_dic'][scent_one]
        if not bag[item_id]['scent_one']:
            bag.pop(item_id)


    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        scent_one = request.POST['scent_one']
        bag = request.session.get('bag', {})
        del bag[item_id]['scent_one_dic'][scent_one]
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)




