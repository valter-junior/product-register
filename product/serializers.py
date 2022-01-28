from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.forms import ModelForm, models
from rest_framework import serializers
from sqlalchemy import true
from .models import Product, Purchase, Sell


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'qtdP', 'qtdS', 'total']

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'product', 'qtd']

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = ['id', 'product', 'qtd']



