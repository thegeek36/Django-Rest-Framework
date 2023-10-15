from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


#ModelViewSet Class Definition
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['name','city']
    search_fields = ['city']
    search_fields = ['^name']





