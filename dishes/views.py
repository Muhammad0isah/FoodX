from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import Dishe
from django.urls import reverse
from django.db.models import Q
from .models import FoodType, RecommendProduct,CartItem


# Create your views here.
def product(request):
    products = Dishe.objects.all()
    trending = FoodType.objects.all()
    recommend_item = RecommendProduct.objects.all()
    context = {'dishes': products, 'trending': trending, 'recommend_item': recommend_item}
    return render(request, 'product.html', context)

def product_list_by_category(request, category):
    products = FoodType.objects.filter(category=category)
    return render(request, 'product_list_by_category.html', {'dishes': products, 'category': category})

def search_products(request):
    query = request.GET.get('key', '')
    products = Dishe.objects.filter(Q(name__icontains=query) | Q(name__iexact=query))
    return render(request, 'search_results.html', {'dishes': products, 'query': query})


def add_to_cart(request, id):
    if request.user.is_authenticated:
        # Assuming you have the Dishe model defined and you get the product using its ID
        product = Dishe.objects.get(id=id)

        # Create and save the new CartItem instance
        cart_item = CartItem(user=request.user, product=product)
        cart_item.save()
    return redirect('product')
    



def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price for item in cart_items)
    else:
        cart_items = []
    return render(request, 'cart.html', {'cart_items': cart_items,'total_price':total_price})
