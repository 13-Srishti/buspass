from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Studentdata(models.Model):
   id= models.AutoField
    eno= models.CharField(max_length=20, default='')
    name= models.CharField(max_length=50, default='')
    sem= models.CharField(max_length=2, default='')
    course= models.CharField(max_length=50, default='')
    add= models.CharField(max_length=50, default='')
    phone= PhoneNumberField(max_length=10, default='')

    def __str__(self):
        return self.eno
