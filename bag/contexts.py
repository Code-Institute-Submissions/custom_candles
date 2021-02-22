from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import products

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    bag = request.session.get('bag',{})

    for item_id, quantity in bag.items():
        product = get_object_or_404(products, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if len(bag_items)>=1:
        delivery = settings.STANDARD_DELIVERY_PRICE
    
        if product_count % settings.PRODUCT_DISCOUNT_THRESHOLD==0:
            discount = 5 * (product_count % settings.PRODUCT_DISCOUNT_THRESHOLD)
        
        else:
            discount = 0  
    
    else:
        delivery = 0
        discount = 0
    
    grand_total = total - discount + delivery
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'grand_total': grand_total,
    }

    return context
