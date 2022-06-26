from rest_framework import serializers
from .models import Product, ProductOrdem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'purchase', 'sales', 'qtdStock', 'cost', 'revenues', 'profit']

class ProductOrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrdem
        fields = ['id', 'product', 'qtd', 'price', 'pOrS']
     

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


