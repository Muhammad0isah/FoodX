from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.urls import reverse
from django.db.models import Q, Sum


# Create your views here.
def event(request):
    event = Event.objects.all()
    context = {'event': event}
    return render(request, 'event.html', context)



def search_products(request):
    query = request.GET.get('key', '')
    products = Event.objects.filter(Q(name__icontains=query) | Q(name__iexact=query))
    return render(request, 'search_results.html', {'event': products, 'query': query})
