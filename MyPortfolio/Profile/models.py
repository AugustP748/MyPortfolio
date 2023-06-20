from django.db import models


# Create your models here.
class PictureProfile(models.Model):
    image = models.ImageField(upload_to='profile/images/')
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    main_image = models.ImageField(upload_to='profile/images/main_image/',default='por_defecto/no_user.jpg')
    curriculum = models.FileField(upload_to='profile/files/cv')
    birth_date = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subtitle = models.TextField()
    description = models.TextField()
    nationality=models.CharField(max_length=20)
    living=models.CharField(max_length=100)
    mission=models.TextField()
    vision = models.TextField()
    call_to_action = models.TextField()
    images = models.ForeignKey(PictureProfile)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Profile"
        verbose_name_plural="Profiles"
       
class Language():
    language_name=models.CharField(max_length=50)
    profile=models.ForeignKey(Profile)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Language"
        verbose_name_plural="Languages"
    
class TypeCharacteristic(models.Model):
    type_charact_name=models.CharField()
    visible=models.BooleanField(default=True)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Type characteristic"
        verbose_name_plural="Types characteristics"
        
class Characteristic(models.Model):
    skill_name=models.CharField(max_length=75)
    description=models.TextField()
    profile=models.ForeignKey(Profile)
    type_charact=models.ForeignKey(TypeCharacteristic)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Characteristic"
        verbose_name_plural="Characteristics"

    
class Education(models.Model):
    institute=models.CharField(max_length=100)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    description=models.TextField()
    image=models.ImageField(upload_to='profile/images/education/')
    icon=models.ImageField(upload_to='profile/images/education/icons')
    profile=models.ForeignKey(Profile)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Education"
        verbose_name_plural="Educations"
        
class course(models.Model):
    title=models.CharField(max_length=120)
    certificate=models.FileField(upload_to='profile/files/education')
    description=models.TextField()
    education=models.ForeignKey(Education)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="course"
        verbose_name_plural="courses"