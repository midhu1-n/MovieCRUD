
# Create your views here.

#DRF methods slighty different from django
from app.models import models,Employee
from app.serializers import EmployeeSerializer

#using generics class--advanced coding fewer lines of coding as compared to APIView
from rest_framework import generics
class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#Apiview creating a new student record

#using generics class
class EmployeeCreate(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# using generics class
class EmployeeDetail(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# using generics class
class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# using generics class
class EmployeeUpdate(generics.UpdateAPIView):
    #put/patch
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


from rest_framework import viewsets
from app.models import Employee
from app.serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):#GET/POST/DELETE/PATCH/PUT
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


