from django.shortcuts import (
    render, redirect)
from product.models import colours, scents


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request):
    """ Add a quantity of the specified product to the shopping bag """

    if request.method == "POST":
     
        bag = {
            "colour_select": request.form.get("colour_select"),
            "scent_one_select ": request.form.get("scent_one_select"),
            "scent_two_select": request.form.get("scent_two_select"),
            "quantity": int(request.form.get("quantity")),
        }


    redirect_url = request.POST.get('redirect_url')
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
