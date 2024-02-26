from rest_framework import serializers
from .models import Patient,Procedure
import base64
# def length_check(value):
#     if len(value)!=10:
#         raise serializers.ValidationError('Length of mobile number should be exaclty 10')

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields='__all__'


class ProcedureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Procedure
        fields='__all__'
    