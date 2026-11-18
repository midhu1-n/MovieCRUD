from django.db.migrations import serializer
from django.db.models import Model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from rest_framework.response import Response

from Expense.serializers import ExpenseSerializer
from rest_framework import status, response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from Expense.models import Expense

# Create your views here.
class ExpenseCreate(APIView):
    authentication_classes = [TokenAuthentication]#to check whether the requested user is valid or not
    permission_classes = [IsAuthenticated]#only logged in user can create expense
    def post(self,request):
      serializer_instance = ExpenseSerializer(data=request.data) #title,amount,category,payment,priority
                                                                  #all fields except user
      if serializer_instance.is_valid():
        serializer_instance.save(user=request.user)
        return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


class Expenselist(APIView):
    authentication_classes = [TokenAuthentication]  # to check whether the requested user is valid or not
    permission_classes = [IsAuthenticated]
    def get(self,request):
        e=Expense.objects.filter(user=request.user)#filters only current user expenses
        serializer_instance=ExpenseSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
