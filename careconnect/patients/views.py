from django.shortcuts import render

# Create your views here.
from patients.models import Appointment
from rest_framework.views import APIView
from rest_framework.response import Response
from patients.serializers import PatientSerializer,AppointmentSerializer
from rest_framework import status, response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated


#Appointment booking view
from datetime import datetime, time, timedelta


class AppointmentCreate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]  #only authenticated users can create appointment
    def post(self,request):
        serializer_instance = AppointmentSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            #token_number
            data=serializer_instance.validated_data
            d=data['doctor']#fetches doctor from client data
            date=data['appointment_date']#fetches data from client data
            token=0
            appointment_time=time(9,0)
            a=Appointment.objects.filter(doctor=d,appointment_date=date).last()
            if a:
                token=a.token_number+1
                appointment_time=(datetime.combine(date,a.appointment_time)+timedelta(minutes=15)).time()
            else:
                token=1
                # time=time

            serializer_instance.save(token_number=token,appointment_time=appointment_time)
            # serializer_instance.save()
            response={
                "status":"booked",
                "booking_data":serializer_instance.data
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

#APIView for creating a User
class PatientRegister(APIView):
    def post(self,request):
        serializer_instance = PatientSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
