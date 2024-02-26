from django.db import models
from django.contrib.auth.models import User



class Patient(models.Model):
    first_name=models.CharField(max_length=10,null=True,default="")
    last_name=models.CharField(max_length=10,null=True,default="")
    mobile_number=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=15,null=True,default="")
    birthdate=models.DateField(blank=True, default='', null=True)
    city=models.CharField(max_length=12,null=True,default="")
    state=models.CharField(max_length=14,null=True,default="")
    pincode=models.CharField(max_length=6,null=True,default="")
    emergency_contant_name=models.CharField(max_length=12,null=True,default="")
    emergency_contant_mobile_number=models.CharField(max_length=10,null=True,default="")
    language=models.CharField(max_length=8,null=True,default="") 

    def __str__(self):
        return str(self.mobile_number)
                                                             
class Procedure(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    patient=models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    status=models.CharField(max_length=50,default="")
    statusReason=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")            
    type=models.CharField(max_length=50,default="")             
    clinic_address=models.CharField(max_length=50,default="")  
    notes=models.CharField(max_length=50,default="")  
    report=models.FileField(null=True,blank=True)

