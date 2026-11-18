from rest_framework import serializers
from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        u=User.objects.create_superuser(**validated_data)
        u.save()
        return u
