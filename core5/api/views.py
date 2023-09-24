#Generic API view and Model Mixin
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

""" Here I have implemented all the Mixins methods in different classes
#ListModelMixin
class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #GET   Method
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
#CreateModelMixin
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #Post Method
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
#RetrieveModelMixin
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #GET Method
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)   
#UpdateModelMixin
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #PUT or PATCH Method
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)   
#DestroyModelMixin
class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #PUT or PATCH Method
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""
#The model mixins is of 2 types 1 : with id 2: without id
#List and Create do not required pk field.
class StudentApiLC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #GET Method 
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #Post Method
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#Retrieve Update and Destroy require pk field.
class StudentAPIRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #GET Method
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)   
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #PUT or PATCH Method
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)   

    queryset = Student.objects.all()
    serializer_class = StudentSerializer    
    #PUT or PATCH Method
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)