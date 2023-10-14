from django.shortcuts import render
from dishes.models import Dishe, RecommendProduct
from dishes.models import FoodType
from news.models import New


# Create your views here.
def index(request):
    products = Dishe.objects.all()
    trending = FoodType.objects.all()
    tech_news = New.objects.all()
    recommend_item = RecommendProduct.objects.all()
    context = {'dishes': products, 'trending': trending, 'news': tech_news,'recommend_item': recommend_item}
    return render(request, 'index.html', context)
