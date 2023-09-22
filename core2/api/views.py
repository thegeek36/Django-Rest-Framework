from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
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

#Mode queryset to get all students
def student_list(request):
    #Mode queryset to get all students
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many = True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type ='application/json')
    return JsonResponse(serializer.data,safe = False)

@csrf_exempt
def create(request): 
    #if post method
    if request.method == 'POST':
        #request the data from frontend
        json_data = request.body
        stream = io.BytesIO(json_data)
        #parse it into pytyon datatype
        pythondata = JSONParser().parse(stream)
        #serialize it into complex data type
        serializer = StudentSerializer(data = pythondata)
        #check if serializeer is valid then save it and send a response.
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")

    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            #json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(serializer.data) 
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg":"Data Saved successfully"}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')  

    if request.method == 'PUT':   
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        stu = Student.objects.get(id = id)
        serializer = StudentSerializer(stu,data = data,partial  = True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "Data  Updated"}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
            return JsonResponse(res,safe=False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')  
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {"msg":"Data deleted successfully"}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')  
        return JsonResponse(res,safe=False)
