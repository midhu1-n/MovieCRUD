from asyncio import mixins

from django.db.migrations import serializer
from django.shortcuts import render, get_object_or_404

# Create your views here.
# from django.http import JsonResponse
#
# from django.views import View



# #To read all records
# class EmployeeList(View):
#     def get(self,request):
#         s=list(Employee.objects.all().values())   #read all data records student table
#         print(s)
#         print(type(s))  #queryset of objects not python native type
#         return JsonResponse(s,safe=False)

#DRF methods slighty different from django
from app.models import models,Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import EmployeeSerializer

# class EmployeeList(APIView):
#     def get(self,request):
#         #reads all employee records from employee table
#         qs= Employee.objects.all()
#         #converts the qs into python native using  Employee serializer
#         serializer_instance=EmployeeSerializer(qs,many=True)
#         #returns response as json using response function
#         print(serializer_instance.data)
#         return Response(serializer_instance.data)

#using mixins class--advanced coding fewer lines of coding as compared to APIView
from rest_framework import mixins,generics
class EmployeeList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request):
        return self.list(request)


#Apiview creating a new student record
# from json import loads

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# @method_decorator(csrf_exempt,name="dispatch")
#
# class EmployeeCreate(View):
#      def post(self,request):
#          #fetches data from client side
#          form_data=request.body  #json data
#          #converts json data into python native type(dictionary)
#          data=loads(form_data)
#          print(data)
#          n=data['name']
#          i=data['empid']
#          a=data['age']
#          p=data['place']
#          g=data['gender']
#          s=data['salary']
#          d=data['designation']
#
#          #creates a new record inside db table
#          #insert into student(name,age,course,marks)values(%s,%s,%s,%s),(n,a,c,m))
#          #orm query
#          #modelname.objects.create(field=value,field=value,...)
#          s=Employee.objects.create(name=n,empid=i,age=a,place=p,gender=g,salary=s,designation=d)
#          #s=Student.objects.create(**data)
#          s.save()
#          #returns Response
#          return JsonResponse({"message":"created"})

# class EmployeeCreate(APIView):
#     def post(self,request):
#         # data=request.data
#         #validation+conversion(native to modelobjects)
#         serializer_instance=EmployeeSerializer(data=request.data)
#         print(request.data)
#
#         #checks whether the data coming from client is valid,if valid
#         #saves the data into model
#         if serializer_instance.is_valid():  #to check validation
#             serializer_instance.save() #saves the data into model
#             return Response(serializer_instance.data) #send created object as response
#         #if data is not valid it will show validation errors
#         else:
#             return Response(serializer_instance.errors)

        e=Employee.objects.create(**data)
        e.save()
        return Response({"message":"created"})

#using mixin class
class EmployeeCreate(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self,request):
        return self.create(request)



#API view for reading particular student record
# class EmployeeDetail(APIView):
#     def get(self,request,i):
#         #reads employee record matching id
#         #e=Employee.objects.get(id=1)#it works fine but it shows error for unknown id we can use try except here
#         e=get_object_or_404(Employee,id=i)  #here if we provide an id that doesnt exist it will sent an 404 found ,instead of showing error
#
#         #calls Employee serializer class for serialization
#         serializer_instance=EmployeeSerializer(e)
#
#         #sends response back to client
#         return Response(serializer_instance.data)

# using mixin class
class EmployeeDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)


#apiview for deleting existing employee record

# class EmployeeDelete(APIView):
#     def delete(self,request,i):
#
#         #reads record matching with id
#         e=get_object_or_404(Employee,id=i)
#         #deletes the record
#         e.delete()
#         #sends
#         return Response({"message":"Deleted"})


# using mixin class

# using mixin class
class EmployeeDelete(mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def delete(self,request,pk):
        return self.destroy(request,pk)

#apiview for updating(fully) existing employee record
# class EmployeeUpdate(APIView):
#     def put(self,request,i):
#         #reads the record matching with id
#         e=get_object_or_404(Employee,id=i)
#         #fetches the data coming from client
#         data=request.data
#         #calls Employee Serializer class for deserialization(validation+conversion)
#         serializer_instance=EmployeeSerializer(instance=e,data=data)
#         if serializer_instance.is_valid():
#            #saves the record
#            serializer_instance.save()
#         #sends response back to client
#            return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)

# using mixin class
class EmployeeUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self,request,pk):
        return self.update(request,pk)


#apiview for updating(partial) existing employee record
# class EmployeePartialUpdate(APIView):
    # def patch(self,request,i):
    #     #reads the record matching with id
    #     e=get_object_or_404(Employee,id=i)
    #     #fetches the data coming from client
    #     data=request.data
    #     #calls Employee Serializer class for deserialization(validation+conversion)
    #     serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)
    #     if serializer_instance.is_valid():
    #        #saves the record
    #        serializer_instance.save()
    #     #sends response back to client
    #        return Response(serializer_instance.data)
    #     else:
    #         return Response(serializer_instance.errors)



# using mixin class
class EmployeePartialUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def patch(self,request,pk):
        return self.partial_update(request,pk)