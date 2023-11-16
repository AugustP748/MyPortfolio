from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='portfolio'
urlpatterns = [
    path('', views.home,name="home"),
    path('download-cv', views.descargar_archivo,name="download-cv"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)