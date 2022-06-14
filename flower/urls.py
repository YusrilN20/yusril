from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import UmumList

urlpatterns = [
    path('s/',views.Umum,name='main'),
    path('',views.FlowerLanding,name='main'),
    path('test/', UmumList.as_view(), name='kosong'),
    # <a href=></a>
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)