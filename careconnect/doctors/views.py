from django.shortcuts import render

# Create your views here.

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from doctors.models import Doctor
from rest_framework.views import APIView
from rest_framework.response import Response

from doctors.permissions import IsAdminUserOrReadOnly
from doctors.serializers import DoctorSerializer,UserSerializer
from rest_framework import status, response
from django.shortcuts import get_object_or_404

# Create your views here.
# API VIEWS for

#Creating doctor

#Reading all doctors
class DoctorListCreateView(APIView):
    authentication_classes = [BasicAuthentication]#username,password
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request):
            qs = Doctor.objects.all()
            serializer_instance = DoctorSerializer(qs, many=True)
            print(serializer_instance.data)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance = DoctorSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorRetrieveUpdateDelete(APIView):
    authentication_classes = [BasicAuthentication]#username,password
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request,pk):
            m = get_object_or_404(Doctor,id=pk)
            self.check_object_permissions(request,m)
            serializer_instance = DoctorSerializer(m)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
            m = get_object_or_404(Doctor,id=pk)
            self.check_object_permissions(request, m)
            serializer_instance = DoctorSerializer(instance=m,data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        m=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request, m)
        serializer_instance=DoctorSerializer(instance=m,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        m = get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request, m)
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# filtering doctors based on specialization
class DoctorFilter(APIView):
    def get(self,request):
       #fetches the keyword from query parameters
        data=request.query_params.get('search')
        # print(data)

       #Read all records matching with the keyword from db table(using filter)
        # m=Doctor.objects.filter(specialization__icontains=data)
        m = Doctor.objects.filter(specialization=data)

        #call Serializer class for Serialization
        serializer_instance=DoctorSerializer(m,many=True)

        #return Response back to client
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#APIView for creating admin user
from rest_framework import serializers
from django.contrib.auth.models import User
class AdminRegister(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
