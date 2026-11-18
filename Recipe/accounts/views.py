from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from rest_framework import status, response
from django.shortcuts import get_object_or_404




class UserRegister(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
