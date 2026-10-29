from rest_framework import serializers
from app.models import Employee
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    empid=serializers.IntegerField()
    age=serializers.IntegerField()
    place=serializers.CharField()
    gender_choices=(('male','Male'),('female','Female'))
    gender=serializers.ChoiceField(choices=gender_choices)
    joining_date=serializers.DateField(read_only=True)
    salary=serializers.IntegerField()
    designation=serializers.CharField()
    image=serializers.ImageField()
    #create() is called after validation and before saving
    def create(self,validated_data):
        print(validated_data)
        e=Employee.objects.create(**validated_data)
        return e
    #after validation before saving
    def update(self,instance,validated_data):
        instance.empid=validated_data.get('empid',instance.empid)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.place = validated_data.get('place', instance.place)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.designation = validated_data.get('designation', instance.designation)

        instance.save()

        return instance


    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError("Age should be positive")

        return data






