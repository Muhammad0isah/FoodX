from django.shortcuts import render
from .models import CustomerReview


# Create your views here.
def news(request):
    tech_news = CustomerReview.objects.all()
    return render(request, 'review.html', {'review': tech_news})

