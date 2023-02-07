
from django.urls import path
from products.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',products.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)