from django.shortcuts import render
from .models import ISADMembers




def member(request):
    members = ISADMembers.objects.all()
    return render(request, 'members.html', {'members': members})