from django.db import models


# Create your models here.
class PictureProfile(models.Model):
    image = models.ImageField(upload_to='profile/images/')
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Language(models.Model):
    language_name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Language"
        verbose_name_plural="Languages"
    
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    main_image = models.ImageField(upload_to='profile/images/main_image/',default='por_defecto/no_user.jpg')
    curriculum = models.FileField(upload_to='profile/files/cv')
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subtitle = models.TextField()
    description = models.TextField()
    nationality=models.CharField(max_length=20)
    living=models.CharField(max_length=100)
    mission=models.TextField()
    vision = models.TextField()
    call_to_action = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Profile"
        verbose_name_plural="Profiles"
       

        
class Skill(models.Model):
    Skill_name=models.CharField(max_length=75)
    description=models.TextField()
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Skill"
        verbose_name_plural="Skills"



class Education(models.Model):
    institute=models.CharField(max_length=100)
    title=models.CharField(max_length=50,blank=True, null=True)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    certificate=models.FileField(upload_to='profile/files/education',blank=True, null=True)
    course=models.BooleanField(default=True)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Education"
        verbose_name_plural="Educations"
        
        
class Role(models.Model):
    role_name=models.CharField(max_length=30)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Role"
        verbose_name_plural="Roles"
    
class Experience(models.Model):
    company=models.CharField(max_length=100)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    start_date=models.DateField(blank=True, null=True)
    end_date=models.DateField(blank=True, null=True)
    description=models.TextField()
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Education"
        verbose_name_plural="Educations"