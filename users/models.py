from django.db import models
from cars.models import Car

# Create your models here.
class Shift(models.Model):
    type = models.CharField(max_length=20,unique=True)
    date_created = models.DateTimeField(auto_created=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.type

class Driver(models.Model):
    name = models.CharField(max_length=40,unique=True)
    image = models.ImageField(upload_to='drivers/images/')
    driving_license = models.ImageField(upload_to='drivers/license')
    category = models.CharField(max_length=4)
    car = models.ManyToManyField(Car,blank=True)
    shift = models.ForeignKey(Shift,on_delete=models.SET_NULL,null=True,blank=True)
    nic = models.CharField(max_length=20,blank=True,unique=True)
    date_created = models.DateTimeField(auto_created=True,auto_now=True)

    def __str__(self):
        return self.name

