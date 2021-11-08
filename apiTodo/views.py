import re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import status



from .serializers import TodoSerializer
from .models import Todo

from rest_framework.decorators import api_view
# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to apiTodo</h1>')

# @api_view(['GET'])
# def todoList(request):
#     queryset = Todo.objects.all()
    
#     serializer=TodoSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def todoListCreate(request):
#         serializer=TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def todoList(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        serializer=TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
# @api_view(['PUT'])
# def todoListUpdate(request,pk):
#     queryset= Todo.objects.get(id=pk)
#     serializer=TodoSerializer(instance=queryset,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def todoListDelete(request,pk):
#     queryset= Todo.objects.get(id=pk)
#     queryset.delete()
#     return Response("Deleted")


@api_view(['GET', 'PUT', 'DELETE'])
def todoDetail(request, pk):
    queryset= Todo.objects.get(id=pk)
    if request.method == 'GET':
        serializer=TodoSerializer(queryset)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer=TodoSerializer(instance=queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    

