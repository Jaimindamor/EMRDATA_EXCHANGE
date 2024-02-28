from django.contrib import admin

from .models import Patient,Procedure

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','mobile_number','address','gender','birthdate','emial','country_code','city',
                  'state','pincode','emergency_contant_name','emergency_contant_mobile_number','language']
    
    
@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display=['id','patient','status','procedure_date','procedure_time','statusReason','category','type','clinic_address','notes','report']