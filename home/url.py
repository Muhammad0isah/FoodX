from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index,about
from event.views import event
from .views import add_comment


urlpatterns = [

]
urlpatterns = [
    path('', index, name='home'),
    path('event/', event, name='event'),
    path('about/', about, name='about'),
    path('add/', add_comment, name='customer_review'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)