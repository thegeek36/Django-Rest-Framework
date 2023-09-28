from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """ We can also write about these classes in settings.py files"""
    #User Authentication Class Definition
    authentication_classes = [BasicAuthentication]
    #User Permission Class
    #permission_classes =  [IsAuthenticated]
    #only isstaf = True user can  access this API
    permission_classes =  [IsAdminUser]


# #ModelViewSet Class Definition
# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     #We can override the  classes defined in settings.py
#     # #User Authentication Class Definition
#     authentication_classes = [BasicAuthentication]
#     # #User Permission Class
#     permission_classes =  [AllowAny]




