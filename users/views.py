from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Users
from .serializers import UsersSerializer                                          
# Create your views here.
authentication_classes = [SessionAuthentication, BasicAuthentication]
permission_classes =[IsAuthenticated]
@csrf_exempt
def user_list(request):
    if request.method =='GET':
        user = Users.objects.all()
        serializer = UsersSerializer(user, many= True)
        return JsonResponse(serializer.data, safe = False)


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
        return JsonResponse(serializer.errors, status =400)  


@csrf_exempt
def user_details(request, pk):
    try:
        userid = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersSerializer(userid)
        return JsonResponse(serializer.data)

    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(Users, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status =400)  


   


