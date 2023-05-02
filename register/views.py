from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import UserSerializer

# Create your views here.

class RegisterView(APIView):
    try:
        def post(self,request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'data': serializer.data,
                    'message':'Account created. Check your email for OTP'
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
