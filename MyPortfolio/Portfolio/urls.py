from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='portfolio'
urlpatterns = [
    path('', views.home,name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)