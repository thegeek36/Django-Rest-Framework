from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .custompermissions import MyPermission
#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """ We can also write about these classes in settings.py files"""
    #User Authentication Class Definition
    authentication_classes = [MyPermission]
    #User Permission Class
    #permission_classes = [IsAuthenticated]

""" 

Custom Permissions
We can create our own custom permissions we have to override BasePerrmissions and Implement either eitherr or both of the following methods:
Cretae a file 
"""





