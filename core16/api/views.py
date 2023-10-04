from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """ We can also write about these classes in settings.py files"""
    #User Authentication Class Definition
    authentication_classes = [JWTAuthentication]
    #User Permission Class
    permission_classes = [IsAuthenticated]
 





