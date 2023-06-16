from django.db import models

# Create your models here.
class Technologie(models.Model):
    name_Tech=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Technologie"
        verbose_name_plural="Technologies"
        
    def __str__(self) -> str:
        return self.name_Tech

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/',default='por_defecto/no_imagen.jpg')
    url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Technologie)
    visible=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Project"
        verbose_name_plural="Projects"
    
    def __str__(self) -> str:
        return self.title + self.url + str(self.visible)