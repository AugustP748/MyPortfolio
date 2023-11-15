from django.shortcuts import render
from Projects.models import Project, Technologie
from Profile.models import Profile, Skill
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.
def home(request):
    #prototipodjango7@gmail.com
    if request.method == 'POST':
        name = request.POST.get('nameInput','')
        phone = request.POST.get('telInput','')
        message = request.POST.get('MensajeTextarea', '')
        from_email = request.POST.get('emailInput', '')
        send_mail(
            "New email from Portfolio from "+name+"!",
            message+name+phone,
            from_email,
            ["prototipodjango7@gmail.com"],
            fail_silently=False,)
        
    # Data from Database 
    context={}
    context['projects'] = Project.objects.all()
    context['technologies'] = Technologie.objects.all()
    context['Are_All_Not_Visible'] = not Project.objects.filter(~Q(visible=False)).exists()
    context['profiles'] = Profile.objects.all()
    context['skills'] = Skill.objects.all()
    return render(request,'home.html',context=context)


"""def Send_Email(request):
    #prototipodjango7@gmail.com
    if request.method == 'POST':
        name = request.POST.get('nameInput','')
        phone = request.POST.get('telInput','')
        message = request.POST.get('MensajeTextarea', '')
        from_email = request.POST.get('emailInput', '')
        send_mail(
            "New email from Portfolio from "+name+"!",
            message+name+phone,
            from_email,
            ["prototipodjango7@gmail.com"],
            fail_silently=False,)"""