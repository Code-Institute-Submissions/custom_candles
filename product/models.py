from django.db import models


class colours(models.Model):
    class Meta:
        verbose_name_plural = 'Colours'
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
 


class scents(models.Model):
    class Meta:
        verbose_name_plural = 'Scents'
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_price(self):
        return self.price