from django.shortcuts import render
from Projects.models import Project
from django.db.models import Q
# Create your views here.
def home(request):
    context={}
    context['projects'] = Project.objects.all()
    context['Are_All_Not_Visible'] = not Project.objects.filter(~Q(visible=False)).exists()
    return render(request,'home.html',context=context)
