from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import UserSerializer,VerifySerializer
from .emails import send_otp
from .models import User

# Create your views here.

class RegisterView(APIView):
    try:
        def post(self,request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                return Response({
                    'data': serializer.data,
                    'message':'Account created. Check your email for OTP'
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)

class VerifyOtpView(APIView):
    try:
        def post(self,request):
            serializer = VerifySerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exist():
                    return Response({
                        message:'something went wrong',data:'invalid email'
                        },
                        status=status.HTTP_400_BAD_REQUEST)  
                if user[0].otp != otp:
                    return Response(
                        {message:'something went wrong',data:'wrong OTP'},
                        status = status.HTTP_400_BAD_REQUEST
                    )
                user = user.first()
                user.isVerified == True
                user.save()
                return Response({
                    message:'account verified',
                    data:{}
                },status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)

