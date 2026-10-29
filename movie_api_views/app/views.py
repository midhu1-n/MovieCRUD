from rest_framework import mixins,generics,viewsets
from app.models import Movie
from app.serializers import MovieSerializer
#using mixins
#apiview for listing and creating movie record
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)

#APIVIEW for read/update/delete existing movie record
# class MovieRetriveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
#                                mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

#using generics class
# class MovieList(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# #Apiview creating a new student record
#
# #using generics class
# class MovieCreate(generics.CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# # using generics class
# class MovieDetail(generics.RetrieveAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# # using generics class
# class MovieDelete(generics.DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# # using generics class
# class MovieUpdate(generics.UpdateAPIView):
#     #put/patch
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


#using Viewsets

class MovieView(viewsets.ModelViewSet):#GET/POST/DELETE/PATCH/PUT
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

