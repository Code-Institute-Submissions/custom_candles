from django.db import models

from product.models import colours, scents

# Create your models here.

class CartItem(models.Model):
    JarColour = models.CharField(max_length=254)
    ScentOne = models.CharField(max_length=254)
    ScentTwo = models.CharField(max_length=254)
    quantity = models.CharField(max_length=254)

    def __unicode__(self):
        return self.JarColour.name

class Cart(models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)

    Total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id) 