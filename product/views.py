from asyncio import exceptions
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from httplib2 import Response
from .models import Product, ProductOrdem
from rest_framework import generics
from .serializers import ProductOrdemSerializer, ProductSerializer, ProductListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ProductCreate(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = Product.objects.all().values('id', 'name')
    serializer_class = ProductListSerializer

    
class MovementList(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = Product.objects.all().values('name', 'purchase', 'sales', 'qtdStock', 'cost', 'revenues', 'profit')
    serializer_class = ProductSerializer
    
class ProductOrdemCreate(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    queryset = ProductOrdem.objects.all()
    serializer_class = ProductOrdemSerializer
    
 
class ProductOrdemList(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = ProductOrdem.objects.all()
    serializer_class = ProductOrdemSerializer



