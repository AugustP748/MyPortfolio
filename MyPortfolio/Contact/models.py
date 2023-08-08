from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    messsage = models.TextField()
    
    class meta:
        verbose_name="Contact"
        verbose_name_plural="Contacts"
        