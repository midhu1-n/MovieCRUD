from django.shortcuts import render

# Create your views here.

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from recipes.models import Recipe
from rest_framework.views import APIView
from rest_framework.response import Response
from recipes.serializers import RecipeSerializer
from rest_framework import status, response
from django.shortcuts import get_object_or_404

# Create your views here.
# API VIEWS for

class RecipeListCreateView(APIView):
    def get(self,request):
            qs = Recipe.objects.all()
            serializer_instance = RecipeSerializer(qs, many=True)
            print(serializer_instance.data)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance = RecipeSerializer(data=request.data)  # deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
            m = get_object_or_404(Recipe,id=pk)
            serializer_instance = RecipeSerializer(m)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
            m = get_object_or_404(Recipe,id=pk)
            serializer_instance = RecipeSerializer(instance=m,data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk):
        m=get_object_or_404(Recipe,id=pk)
        serializer_instance=RecipeSerializer(instance=m,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        m = get_object_or_404(Recipe,id=pk)
        m.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.db.models import Q
#Search apiview
class SearchAPIView(APIView):
    def get(self,request):
       #fetches the keyword from query parameters
        data=request.query_params.get('search')
        print(data)

       #Read all records matching with the keyword from db table(using filter)
        m=Recipe.objects.filter(Q(recipe_name__icontains=data)    |
                               Q(ingredients__icontains=data))
                               # Q(year__icontains=data))

        #call Serializer class for Serialization
        serializer_instance=RecipeSerializer(m,many=True)

        #return Response back to client
        return Response(serializer_instance.data)

