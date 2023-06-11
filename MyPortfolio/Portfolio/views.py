from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    context={}
    context['projects'] = Project.objects.all()
    return render(request,'home.html',context=context)