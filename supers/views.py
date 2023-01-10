from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view (['GET', 'POST'])
def supers_list (request):
   if request.method == 'GET':
    supers_var = Supers.objects.all()
    serializer = SuperSerializer (supers_var, many = True)
    return Response (serializer.data)

   elif request.method == 'POST':
    serializer = SuperSerializer (data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save() 
    return Response (serializer.data, status=status.HTTP_201_CREATED)

    

@api_view (['GET', 'PUT', 'DELETE'])
def supers_detail (request, pk):
   supers_var = get_object_or_404 (Supers, pk=pk)
   if request.method == 'GET':
      serializer = SuperSerializer(super);
      return Response (serializer.data)
   elif request.method == 'PUT':
      serializer = SuperSerializer (supers_var, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response (serializer.data)
   elif request.method == 'DELETE':
      supers_var.delete()
      return Response (status=status.HTTP_204_NO_CONTENT)

      






