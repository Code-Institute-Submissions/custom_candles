from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import products

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(products, pk=item_id)
        for scent_one, quantity in item_data['scent_one_dic'].items():
            total += quantity * product.price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'scent_one': scent_one,
            })

    if len(bag_items)>=1:
        delivery = settings.STANDARD_DELIVERY_PRICE
    
        if quantity / settings.PRODUCT_DISCOUNT_THRESHOLD>=1:
            discount = 5 * round(product_count / settings.PRODUCT_DISCOUNT_THRESHOLD)
        
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
