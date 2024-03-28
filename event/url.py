from django.urls import path
from . import views
from .views import search_products

urlpatterns = [
    path('', views.event, name='event'),
    path('search/', search_products, name='search_products'),
]