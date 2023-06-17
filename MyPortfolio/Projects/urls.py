from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='projects'
urlpatterns = [
    path('projects/', views.home_projects,name="home_projects"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)