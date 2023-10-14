from django.urls import path 
from .views import signup, login
from dishes.views import product

urlpatterns = [
    # path('product/', product,name='product'),
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
]