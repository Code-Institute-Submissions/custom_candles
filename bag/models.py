from django.db import models
from product.models import products, scents

# Create your models here.


class Cart(models.Model):
    products = models.ManyToManyField(products, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Cart id %s" %(self.id)