from rest_framework import serializers
from .models import Patient,Procedure

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields='__all__'

class ProcedureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Procedure
        fields='__all__'
    