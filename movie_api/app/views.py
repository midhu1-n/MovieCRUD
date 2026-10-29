from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from app.serializers import MovieSerializer
from rest_framework.response import Response
from app.models import  Movie
from rest_framework import status
# from app.models import models,Movie


# Create your views here.
#Apiview for creating new movierecord
class MovieCreate(APIView):
    def post(self,request):
        serializer_instance=MovieSerializer(data=request.data) #deserialization
                                                               #conversion+validation
        if serializer_instance.is_valid():
            print(serializer_instance.validated_data)#to view the validated data
            director=serializer_instance.validated_data['director']#to print the specific field in the validated data
            print(director)
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


#APIVIEW for reading all movierecords
class MovieList(APIView):
    def get(self,request):
        #reads all employee records from employee table
        qs= Movie.objects.all()
        #converts the qs into python native using  Employee serializer
        serializer_instance=MovieSerializer(qs,many=True)
        #returns response as json using response function
        print(serializer_instance.data)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#API view for reading a specific movie record

class MovieDetail(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(m)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

#API View for updating a particular record
class MovieUpdate(APIView):
    def put(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(instance=m,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

#Apiview for partially updating a movie record
class MoviePartialUpdate(APIView):
    def patch(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(instance=m,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


#APIView for deleting a movie record
class MovieDelete(APIView):
    def delete(self,request,i):
        m = get_object_or_404(Movie, id=i)
        m.delete()
        return Response({"message:deleted"},status=status.HTTP_204_NO_CONTENT)



