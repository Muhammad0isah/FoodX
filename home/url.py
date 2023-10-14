from django.urls import path
from .views import index
from dishes.views import product

urlpatterns = [
    path('', index, name='home'),
    path('/product',name='product')
]
