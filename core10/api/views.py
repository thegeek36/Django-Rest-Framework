from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions

#ModelViewSet Class Definition
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    """ We can also write about these classes in settings.py files"""
    #User Authentication Class Definition
    authentication_classes = [SessionAuthentication]
    #User Permission Class
    #permission_classes = [IsAuthenticated]
    #only isstaff = True user can  access this API
    #permission_classes =  [IsAdminUser]
    #permission_classes =  [IsAuthenticatedOrReadOnly]
    #permission_classes =  [DjangoModelPermissions]
    permission_classes =  [DjangoObjectPermissions]
    permission_classes =  [DjangoModelPermissionsOrAnonReadOnly]

""" 
The DjangoModelPermissions follows the permission of the Django Model we can chage the  permissions according to our needs.


DjangoModelPermissionsOrAnonReadOnly is similar to DjangoModelPermissions but also allows unauthenticated users to have read-only access to the API


The #IsAuthenticatedOrReadOnly will allow authenticated users to perform any requests.
Request of unauthorised users will only be permitted if the request method is one of the "safe" methods: GET,HEAD,OPTIONS
ReadOnly OPTIONS.

Custom Permissions
We can create our own custom permissions we have to override BasePerrmissions and Implement either eitherr or both of the following methods:
Cretae a file 
"""





