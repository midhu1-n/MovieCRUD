from rest_framework import serializers
from info.models import Student

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    Name=serializers.CharField()
    Age=serializers.IntegerField()
    Course=serializers.CharField()
    Marks=serializers.IntegerField()
    def create(self,validated_data):
        print(validated_data)
        e=Student.objects.create(**validated_data)
        return e
        # after validation before saving

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Course = validated_data.get('Course', instance.Course)
        instance.Marks = validated_data.get('Marks', instance.Marks)
        instance.save()

        return instance