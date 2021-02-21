from django.contrib import admin
from .models import scents, products

# Register your models here.


class scentsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
    )

 


class productsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
        'price',
    )


admin.site.register(scents, scentsAdmin)
admin.site.register(products, productsAdmin)
