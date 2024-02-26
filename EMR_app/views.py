from rest_framework.response import Response
from rest_framework.views import APIView
from .custompermission import Mypermission,Procedurepermission
from .models import Patient,Procedure
from .serializers import PatientSerializer,ProcedureSerializer
import base64
# Create your views here.
class PatientAPI(APIView):
    permission_classes=[Mypermission]
    def get(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            patient=Patient.objects.get(id=id)
            serializer=PatientSerializer(patient)
            return Response(serializer.data)
   
    def put(self,request,format=None):
        pythondata=request.data
        id=request.data.get('id')
        if id is not None:
            patient=Patient.objects.get(id=id)
            serializer=PatientSerializer(patient,data=pythondata,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response("{msg: None}")

    def post(self,request,format=None): 
        python_data=request.data
        
        serializer=PatientSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':' data saved !!!!!!!!!!!'}
            return Response(res)
        return Response(serializer.errors)
    
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            patient=Patient.objects.get(id=id)
            patient.delete()
            return Response("Data deleted !!!!!!!!")

class ProcedureAPI(APIView):
    permission_classes=[Procedurepermission]
    def get(self,request,format=None):
        id=request.data.get('id')  
        procedure=Procedure.objects.get(id=id)
        serializer=ProcedureSerializer(procedure)
        x=serializer['report'].value
        x=x.encode('utf-8')
        x=base64.b64encode(x)
        new_serializer =serializer.data
        new_serializer['new_report']=x.decode() 
        return Response(new_serializer)

    def put(self,request,format=None):
        pythondata=request.data
        if request.FILES:
            pythondata['report']=request.FILES['report']
        id=request.data.get('id')
        if id is not None:
            procedure=Procedure.objects.get(id=id)
            serializer=ProcedureSerializer(procedure,data=pythondata,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    def post(self,request,format=None): 
        python_data=request.data
        python_data['user']=request.user.id
        serializer=ProcedureSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':' data saved !!!!!!!!!!!'}
            return Response(res)
        return Response(serializer.errors)
    
    def delete(self,request,format=None):
        id=request.data.get('id')
        if id is not None:
            patient=Procedure.objects.get(id=id)
            patient.delete()
            return Response("Data deleted !!!!!!!!")