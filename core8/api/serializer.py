from rest_framework import serializers
from .models import Student
    
#Model Serializer
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        #fields = ['id','name','roll','city']
        fields = '__all__'
        #exclude = ['name']
        #Multiple read only feilds
        #read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only':False},
        #                 'roll':{'required':True}}
   
   