from django.contrib import admin
from .models import scents, product

# Register your models here.


class scentsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
    )

 


class productAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
        'price',
    )


admin.site.register(scents, scentsAdmin)
admin.site.register(product, productAdmin)
