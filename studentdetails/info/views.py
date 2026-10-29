from django.shortcuts import render, get_object_or_404
from info.models import models,Student
from rest_framework.views import APIView
from rest_framework.response import Response
from info.serializers import StudentSerializer

#To read all records
class StudentList(APIView):
    def get(self,request):
        qs =Student.objects.all()
        serializer_instance = StudentSerializer(qs, many=True)
        print(serializer_instance.data)
        return Response(serializer_instance.data)



#Apiview creating a new student record


class StudentCreate(APIView):

     def post(self,request):
         serializer_instance = StudentSerializer(data=request.data)
         print(request.data)
         if serializer_instance.is_valid():  # to check validation
             serializer_instance.save()  # saves the data into model
             return Response(serializer_instance.data)  # send created object as response
         # if data is not valid it will show validation errors
         else:
             return Response(serializer_instance.errors)

#API view for reading particular student record
class StudentDetail(APIView):
    def get(self,request,i):
        #reads employee record matching id
        #e=Employee.objects.get(id=1)#it works fine but it shows error for unknown id we can use try except here
        e=get_object_or_404(Student,id=i)  #here if we provide an id that doesnt exist it will sent an 404 found ,instead of showing error

        #calls Employee serializer class for serialization
        serializer_instance=StudentSerializer(e)

        #sends response back to client
        return Response(serializer_instance.data)


#apiview for deleting existing employee record

class StudentDelete(APIView):
    def delete(self,request,i):

        #reads record matching with id
        e=get_object_or_404(Student,id=i)
        #deletes the record
        e.delete()
        #sends
        return Response({"message":"Deleted"})

#apiview for updating(fully) existing employee record
class StudentUpdate(APIView):
    def put(self,request,i):
        #reads the record matching with id
        e=get_object_or_404(Student,id=i)
        #fetches the data coming from client
        data=request.data
        #calls Employee Serializer class for deserialization(validation+conversion)
        serializer_instance=StudentSerializer(instance=e,data=data)
        if serializer_instance.is_valid():
           #saves the record
           serializer_instance.save()
        #sends response back to client
           return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


#apiview for updating(fully) existing employee record
class StudentPartialUpdate(APIView):
    def patch(self,request,i):
        #reads the record matching with id
        e=get_object_or_404(Student,id=i)
        #fetches the data coming from client
        data=request.data
        #calls Employee Serializer class for deserialization(validation+conversion)
        serializer_instance=StudentSerializer(instance=e,data=data,partial=True)
        if serializer_instance.is_valid():
           #saves the record
           serializer_instance.save()
        #sends response back to client
           return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)