from django.urls import path 
from .views import signup, login
from event.views import event

urlpatterns = [
    # path('event/', event,name='event'),
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
]