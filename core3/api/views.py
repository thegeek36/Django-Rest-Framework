from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# @api_view()
#Default is GET 
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello World'})

#Function Based API views.
@api_view(['POST','GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':'GET Request'})
    if request.method == 'POST':
        #data from frontend
        print(request.data)
        return Response({'msg':'POST Request','Data':request.data})

#CRUD API using function based API views. 
""" 
@api_view(['GET','POST','PATCH','DELETE'])
def student_api(request):
    #GET request
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu) 
            return Response(serializer.data)
        stu = Student.objects.all()
        #many = True as it is a queryset
        serializer = StudentSerializer(stu,many = True)
        return Response(serializer.data)
    
    #POST Request
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"})
        return Response(serializer.errors)
    
    #PUT Request
    if request.method == 'PUT':
        #get the Id of the record
        id = request.data.get('id')
        #get the record
        stu = Student.objects.get(id=id)
        #serialize the modelobject
        serializer = StudentSerializer(stu,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated"})
        return Response(serializer.errors)

    #DELETE data
    if request.method == 'DELETE':
        id  = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
"""

#CRUD Browsable APIs using function based API views.
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def student_detail(request,pk=None):
    #GET request
    if request.method == 'GET':
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
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    #PUT Request
    if request.method == 'PUT':
        #get the Id of the record
        id = pk
        #get the record
        stu = Student.objects.get(id=id)
        #serialize the modelobject
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete Data Updated"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    #PATCH Request
    if request.method == 'PATCH':
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
    if request.method == 'DELETE':
        id  = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({"msg": "Data Deleted"},status=status.HTTP_200_OK)

