from django.db import models

# Create your models here.
class SectionPorfolio(models.Model):
    section_name = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Section"
        verbose_name_plural="Sections"