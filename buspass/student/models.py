from django.db import models

# Create your models here.
class Studentdata(models.Model):
    id= models.AutoField
    eno= models.CharField(max_length=20, default='')
    name= models.CharField(max_length=50, default='')
    year= models.IntegerField(default=1)
    branch= models.CharField(max_length=50, default='')

    def __str__(self):
        return self.eno
