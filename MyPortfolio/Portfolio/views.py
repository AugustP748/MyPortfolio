from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from Projects.models import Project, Technologie
from Profile.models import Profile, Skill, Education
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
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
    context['profiles'] = get_object_or_404(Profile, pk=1)
    context['skills'] = Skill.objects.all()
    context['education'] = Education.objects.filter(course=False,visible=True)
    context['courses'] = Education.objects.filter(course=True,visible=True)
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

def descargar_archivo(request):
    profile = get_object_or_404(Profile, pk=1)
    
    # Acceder al campo FileField en tu modelo y obtener la ruta del archivo
    ruta_archivo = profile.curriculum.path
    
    # Leer el archivo y configurar la respuesta para descargarlo
    #with open(ruta_archivo, 'rb') as archivo:
    #    response = HttpResponse(archivo.read())
    #    response['Content-Type'] = 'application/force-download'
    #    response['Content-Disposition'] = 'attachment; filename=' + 'CV_Paz_Augusto.pdf'
    #    return response
    archivo = open(ruta_archivo, 'rb')
    return FileResponse(archivo, content_type='application/pdf')