from lib2to3.pgen2.parse import ParseError
from django.db import models
from rest_framework import serializers


bnull = dict(blank=True, null=True)

objStatus = (('P', 'Purchase'), ('S', 'Sales'))

class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    purchase = models.FloatField(default=0.0)
    sales = models.FloatField(default=0.0)
    qtdStock = models.FloatField(default=0.0)
    cost = models.FloatField(default=0.0)
    revenues = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class ProductOrdem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, **bnull)
    qtd = models.FloatField(**bnull)
    price = models.FloatField(**bnull)
    pOrS = models.CharField(max_length=100, choices=objStatus)

    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.pOrS == 'P':
            self.product.purchase += self.qtd
            self.product.cost += self.qtd * self.price
            self.product.qtdStock = self.product.purchase - self.product.sales
            self.product.profit = self.product.revenues - self.product.cost
            self.product.save()
            super(ProductOrdem, self).save(force_insert, force_update, *args, **kwargs)
        elif self.pOrS == 'S':
            if self.qtd <= self.product.qtdStock:          
                self.product.sales += self.qtd
                self.product.revenues += self.qtd * self.price
                self.product.qtdStock = self.product.purchase - self.product.sales
                self.product.profit = self.product.revenues - self.product.cost
                self.product.save()
                super(ProductOrdem, self).save(force_insert, force_update, *args, **kwargs)
            elif self.qtd > self.product.qtdStock:
                stock = self.product.qtdStock
                raise serializers.ValidationError(f"Stock not available, quantity available is {stock}")
                

    