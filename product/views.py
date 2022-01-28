from itertools import product
from xml.dom.minidom import Element
from django.shortcuts import render
from sqlalchemy import null
from .models import Product, Purchase, Sell
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import ProductSerializer, PurchaseSerializer, SellSerializer
from rest_framework.response import Response



class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all(),
    serializer_class = ProductSerializer
      

    
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class PurchaseCreate(generics.CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseList(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SellCreate(generics.CreateAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

