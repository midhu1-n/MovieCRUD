from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.views import APIView,status
from rest_framework.response import Response
from accounts.serializers import UserSerializer


class UserRegister(APIView):
    def post(self,request):
        serializer_instance =UserSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        return Response({"message":"logout sucessfully"},status=status.HTTP_200_OK)
