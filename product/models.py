from django.db import models


class scents(models.Model):
    class Meta:
        verbose_name_plural = 'Scents'
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    def get_description(self):
        return self.description


class products(models.Model):
    class Meta:
        verbose_name_plural = 'Products'
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    has_scent = models.ManyToManyField(scents, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def __unicode__(self):
        return self.name