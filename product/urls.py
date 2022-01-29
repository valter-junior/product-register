from django import views
from django.urls import path
from .views import ProductCreate, MovementList, ProductList, ProductOrdemCreate, ProductOrdemList

urlpatterns = [
    path('create', ProductCreate.as_view(), name='create-product'),
    path('list', ProductList.as_view(), name='list-product'),
    path('movement', MovementList.as_view()),
    path('ordem', ProductOrdemCreate.as_view(), name='create-purchase'),
    path('ordem-list', ProductOrdemList.as_view()),
    
]
