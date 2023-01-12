from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers
from django.shortcuts import get_object_or_404
from super_types.models import SuperType
from super_types.serializer import SuperTypeSerializer

# Create your views here.
@api_view (['GET', 'POST'])
def supers_list (request):
   if request.method == 'GET':

      type = request.query_params.get('type')

      supers_var = Supers.objects.all()
      super_types = SuperType.objects.all()
      super_serializer = SuperSerializer (supers_var, many = True)
      super_type_serializer = SuperTypeSerializer (super_types, many=True)
      hero = Supers.objects.filter(super_type__type = 'hero')
      hero_serializer = SuperSerializer(hero, many=True)
      villain = Supers.objects.filter(super_type__type='villain')
      villain_serializer = SuperSerializer(villain, many=True)
      custom_response_dict = {
         'hero': hero_serializer.data, 
         'villain': villain_serializer.data
      }
      if type == "hero":
         supers_var = hero
         return Response (hero_serializer.data)
      elif type == "villain":
         supers_var = villain
         return Response (villain_serializer.data)
      else:
         return Response (custom_response_dict)

   elif request.method == 'POST':
    serializer = SuperSerializer (data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save() 
    return Response (serializer.data, status=status.HTTP_201_CREATED)

    

@api_view (['GET', 'PUT', 'DELETE'])
def supers_detail (request, pk):
   supers_var = get_object_or_404 (Supers, pk=pk)
   if request.method == 'GET':
      serializer = SuperSerializer(supers_var);
      return Response (serializer.data)
   elif request.method == 'PUT':
      serializer = SuperSerializer (supers_var, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response (serializer.data)
   elif request.method == 'DELETE':
      supers_var.delete()
      return Response (status=status.HTTP_204_NO_CONTENT)


      






