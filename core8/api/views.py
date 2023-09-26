from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets

#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#ReadOnlyModelViewSet Class Definition
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
