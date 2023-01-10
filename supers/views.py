from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Supers

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

    


