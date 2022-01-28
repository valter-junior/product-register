from django import views
from django.urls import path
from .views import ProductCreate, ProductList, PurchaseCreate, PurchaseList, SellCreate

urlpatterns = [
    path('purchase', PurchaseCreate.as_view(), name='create-purchase'),
    path('create', ProductCreate.as_view(), name='create-product'),
    path('', ProductList.as_view()),
    path('purchase/', PurchaseList.as_view()),
    path('sell', SellCreate.as_view())
    
]
