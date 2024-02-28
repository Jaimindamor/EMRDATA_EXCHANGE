from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Patient(models.Model):
    first_name=models.CharField(blank=True,max_length=30,null=True)
    last_name=models.CharField(blank=True,max_length=30,null=True)
    mobile_number=models.CharField(blank=True,max_length=10,null=True)
    address=models.CharField(max_length=255,blank=True,null=True,default="")
    gender=models.CharField(blank=True,max_length=15,null=True)
    birthdate=models.DateField(blank=True, null=True)
    emial=models.EmailField(blank=True, null=True,default="")
    country_code=models.CharField(blank=True,max_length=3,null=True,default="")
    city=models.CharField(blank=True,max_length=12,null=True)
    state=models.CharField(blank=True,max_length=14,null=True)
    pincode=models.CharField(blank=True,max_length=6,null=True)
    emergency_contant_name=models.CharField(blank=True,max_length=12,null=True)
    emergency_contant_mobile_number=models.CharField(blank=True,max_length=10,null=True)
    language=models.CharField(blank=True,max_length=8,null=True)
    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    def save(self, *args, **kwargs):    
        self.update_date = timezone.now()
        super(Patient, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.mobile_number)
                                                             
class Procedure(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    patient=models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    status=models.CharField(blank=True,max_length=50)
    statusReason=models.CharField(blank=True,max_length=50)
    procedure_date=models.DateField(blank=True, null=True)
    procedure_time=models.TimeField(blank=True, null=True)
    category=models.CharField(blank=True,max_length=50)            
    type=models.CharField(blank=True,max_length=50)             
    clinic_address=models.CharField(blank=True,max_length=50)  
    notes=models.CharField(blank=True,max_length=50)  
    report=models.FileField(null=True,blank=True)

    create_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    def save(self, *args, **kwargs):    
        self.update_date = timezone.now()
        super(Procedure, self).save(*args, **kwargs)

