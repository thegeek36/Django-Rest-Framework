from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse,JsonResponse
# Create your views here.

#Model-Object Single Student Data Row wise

def student_detail(request,pk):
    #Mode Object
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    #return HttpResponse(json_data,content_type ='application/json')
    return JsonResponse(serializer.data,safe = True)

def student_list(request):
    #Mode queryset
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many = True)
    print(serializer)
    print("###################################################")
    print(serializer.data)
    print("###################################################")
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type ='application/json')