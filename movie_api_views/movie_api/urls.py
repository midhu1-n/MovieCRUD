"""
URL configuration for movie_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.views import APIView

from app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('movies',views.MovieListCreate.as_view()),
#     path('movies/<int:pk>',views.MovieRetriveUpdateDelete.as_view())
#
# ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('list',views.MovieList.as_view()),
#     path('create',views.MovieCreate.as_view()),
#     path('details/<int:pk>',views.MovieDetail.as_view()),
#     path('delete/<int:pk>',views.MovieDelete.as_view()),
#     path('update/<int:pk>',views.MovieUpdate.as_view()),
#
# ]

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('movies',views.MovieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))

]

