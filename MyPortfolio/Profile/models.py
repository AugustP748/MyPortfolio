from django.db import models

class Skill(models.Model):
    skill_name=models.CharField(max_length=75)
    description=models.TextField()
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Skill"
        verbose_name_plural="Skills"

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile/images/',default='por_defecto/no_user.jpg')
    birth_date = models.DateTimeField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    mission=models.TextField()
    vision = models.TextField()
    call_to_action = models.TextField()
    skills_list = models.ForeignKey(Skill)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Profile"
        verbose_name_plural="Profiles"