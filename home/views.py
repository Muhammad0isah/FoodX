from django.shortcuts import render, redirect
from event.models import Event
from home.models import HeroSection
from .forms import CommentForm
from .models import UserComment

# Create your views here.
def index(request):
    event = Event.objects.all()
    comments = UserComment.objects.all()
    hero_sections = HeroSection.objects.all()
    context = {'event': event,'hero_sections': hero_sections,'member': comments}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def add_comment(request):
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        print('Add member')
        if comment_form.is_valid():
            comment_form.save()
            return redirect('home')
    else:
        print('something wrong')
    context = {
        "review_form": comment_form
    }
    return render(request, 'add_comment.html', context)