from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView


#ModelViewSet Class Definition
class StudentList(ListAPIView):
    queryset = Student.objects.all
    serializer_class = StudentSerializer
    def  get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby = user)





