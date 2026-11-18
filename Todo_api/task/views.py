

# Create your views here.
# from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from task.models import task
from rest_framework.views import APIView
from rest_framework.response import Response

from task.permissions import Custom
from task.serializers import TodoSerializer
from rest_framework import status, response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
# Create your views here.
# API VIEWS for
class TodoListCreateView(APIView):
    authentication_classes = [TokenAuthentication]#username,password
    permission_classes = [IsAuthenticated]
    def get(self,request):
            qs = task.objects.filter(user=request.user)
            serializer_instance = TodoSerializer(qs, many=True)
            print(serializer_instance.data)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance = TodoSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]#username,password
    permission_classes = [IsAuthenticated,Custom]
    def get(self,request,pk):
            m = get_object_or_404(task,id=pk)
            self.check_object_permissions(request,m)
            serializer_instance = TodoSerializer(m)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
            m = get_object_or_404(task,id=pk)
            self.check_object_permissions(request, m)
            serializer_instance = TodoSerializer(instance=m,data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        m=get_object_or_404(task,id=pk)
        self.check_object_permissions(request, m)
        serializer_instance=TodoSerializer(instance=m,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        m = get_object_or_404(task,id=pk)
        self.check_object_permissions(request, m)
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)