from rest_framework import serializers
from patients.models import Appointment


from django.contrib.auth.models import User

from datetime import datetime
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['id','appointment_time', 'token_number', 'created_at']

    def validate(self,validated_data):
        appointment_date=validated_data['appointment_date']
        todays_date=datetime.now().date()
        d=validated_data['doctor']

        if appointment_date<todays_date:
            raise serializers.ValidationError("Invalid Date")

        booked_slots=Appointment.objects.filter(doctor=d,appointment_date=appointment_date).last()
        if booked_slots:
            if booked_slots.token_number==25:
              raise serializers.ValidationError("slot is full")

        return validated_data
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u
