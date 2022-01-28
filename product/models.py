from itertools import product
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models
from sqlalchemy import null

bnull = dict(blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=40)
    qtdP = models.FloatField(**bnull)
    qtdS = models.FloatField(**bnull)
    total = models.FloatField(**bnull)

    def __str__(self):
        return self.name

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **bnull)
    qtd = models.FloatField(**bnull)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.product.qtdP += self.qtd
        self.product.total = self.product.qtdP - self.product.qtdS
        self.product.save()
        super(Purchase, self).save(force_insert, force_update, *args, **kwargs)
    
class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **bnull)
    qtd = models.FloatField(**bnull)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.product.qtdS += self.qtd
        self.product.total = self.product.qtdP - self.product.qtdS
        self.product.save()
        super(Sell, self).save(force_insert, force_update, *args, **kwargs) 
   
