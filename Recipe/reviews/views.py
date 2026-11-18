from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework.views import APIView

from reviews import serializers
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from reviews.models import Review
class CreateReview(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.user)
        u=request.user #current user object
        serializer_instance=ReviewSerializer(data=request.data)


        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import get_object_or_404
class ReviewRecipe(APIView):
    def get(self,request,pk):
      qs=Review.objects.filter(recipe=pk)
      serializer_instance=ReviewSerializer(qs,many=True)
      return Response(serializer_instance.data,status=status.HTTP_200_OK)


from reviews.permissions import IsOwner

class ReviewUpdate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    def put(self,request,pk):
            r = get_object_or_404(Review, id=pk)
            self.check_object_permissions(request,r) #manually checks if requested user has permissions to
            #perform the following operation on review object r
            serializer_instance = ReviewSerializer(instance=r, data=request.data)
            if serializer_instance.is_valid():
                serializer_instance.save()
                return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewDelete(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    def delete(self, request, pk):
            r= get_object_or_404(Review,id=pk)
            self.check_object_permissions(request, r)
            r.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


