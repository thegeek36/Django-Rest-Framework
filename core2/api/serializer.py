from rest_framework import serializers
from .models import Student



    
#Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    #Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name should  start with r") 
    #Validator for name we cannot update it because read_ony is true.
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        #fields = __all__
        #exclude = ['name']
        #Multiple read only feilds
        #read_only_fields = ['name','roll']
        extra_kwargs = {'name':{'read_only':False},
                        'roll':{'required':True}}
    #Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value
    
    #Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'simran' and ct.lower() != 'rourkela':
            raise serializers.ValidationError("City must be Rourkela")
        return data
   
   