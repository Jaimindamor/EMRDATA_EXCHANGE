from django.db import models
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
import re

def check_mobile_number(value):
    reg=r'[1-9]{1}[0-9]{9}'
    if re.findall(reg,value):
        return True
    else:
        raise ValidationError('Not satisfing the condition of (integer value) or (len of number should be 10)')

def check_gender(value):
    reg=r'male|female|others|Not determined'
    if re.search(reg,value):
        return True
    else:
        raise ValidationError('Gender not metioned properly : (male|female|others|Not determined) ')

def check_pincode(value):
    reg=r'^[1-9]{1}[0-9]{5}'
    if re.search(reg,value):
        return True
    else:
        raise ValidationError('Pincode is not correct !!!!!!!!')

def check_emial(value):
    reg=r'[\w]*@[\w]*\.com$'
    if re.search(reg,value):
        return True
    else:
        raise ValidationError('not a validate emial_id !!!!!!!!')



gender_choice=(
    ("male","male"),
    ("female","female"),
    ("others","others")
    
)

# Create your models here.


class Patient(models.Model):
    first_name=models.CharField(blank=True,max_length=30,null=True)
    last_name=models.CharField(blank=True,max_length=30,null=True)
    mobile_number=models.CharField(blank=True,max_length=10,null=True,validators=[MinLengthValidator(10)])
    address=models.CharField(max_length=255,blank=True,null=True)
    gender=models.CharField(blank=True,max_length=15,null=True,choices=gender_choice)
    birthdate=models.DateField(blank=True,null=True)
    emial=models.EmailField(blank=True, null=True)
    country_code=models.CharField(blank=True,max_length=3,null=True)
    city=models.CharField(blank=True,max_length=12,null=True)
    state=models.CharField(blank=True,max_length=14,null=True)
    pincode=models.CharField(blank=True,max_length=6,null=True,validators=[MinLengthValidator(6)])
    emergency_contant_name=models.CharField(blank=True,max_length=12,null=True)
    emergency_contant_mobile_number=models.CharField(blank=True,max_length=10,null=True,validators=[MinLengthValidator(10)])
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

