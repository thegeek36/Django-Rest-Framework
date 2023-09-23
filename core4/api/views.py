from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

#Class Based API views.
#CRUD Browsable APIs using class based API views.
class StudentAPI(APIView):
    #GET request
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu) 
            return Response(serializer.data)
        stu = Student.objects.all()
        # many = True as it is a queryset
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)
    
    #POST Request
    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    #PUT Request
    def put(self,request,pk,format=None):
        #get the Id of the record
        id = pk
        #get the record
        stu = Student.objects.get(id=id)
        #serialize the modelobject
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated"})
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    #PATCH Request
    def patch(self,request,pk,format=None): 
        #get the Id of the record
        id = pk
        #get the record
        stu = Student.objects.get(id=id)
        #serialize the modelobject
        serializer = StudentSerializer(stu,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial Data Updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    #DELETE data
    def delete(self,request,pk,format=None):
        id  = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})

