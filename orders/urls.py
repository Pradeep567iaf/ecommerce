from django.urls import path
from orders.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',orders.as_view())
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)