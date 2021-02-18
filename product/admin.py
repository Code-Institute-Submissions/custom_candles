from django.contrib import admin
from .models import scents, colours

# Register your models here.

class scentsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',     
    )

    ordering = ('sku',)

class coloursAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',  
    )

    ordering = ('sku',)


admin.site.register(scents, scentsAdmin)
admin.site.register(colours, coloursAdmin)
