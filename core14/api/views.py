from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """ We can also write about these classes in settings.py files"""
    #User Authentication Class Definition
    authentication_classes = [TokenAuthentication]
    #User Permission Class
    permission_classes = [IsAuthenticated]
 





