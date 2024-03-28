from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from member.views import member

urlpatterns = [
    path('', member, name='member'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)