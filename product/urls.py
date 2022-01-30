from django.urls import path
from .views import ProductCreate, MovementList, ProductDelete, ProductList, ProductOrdemCreate, ProductOrdemList, ProductUpdate

urlpatterns = [
    path('create', ProductCreate.as_view(), name='create-product'),
    path('list', ProductList.as_view(), name='list-product'),
    path('movement', MovementList.as_view()),
    path('ordem', ProductOrdemCreate.as_view(), name='create-purchase'),
    path('ordem-list', ProductOrdemList.as_view()),
    path('update/<int:pk>', ProductUpdate.as_view()),
    path('delete/<int:pk>', ProductDelete.as_view())
    
]
