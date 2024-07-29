from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializer import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderes
from rest_framework.permissions import IsAuthenticated


#Generate token manualy
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#registraton 
class UserRegistrationView(APIView):
    renderer_classes =[UserRenderes]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({"token" : token, "message" : "Registration Success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#login 
class LoginView(APIView):
    renderer_classes =[UserRenderes]
    def post(self, request, format = None):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email, password= password)

            if user is not None:
                token = get_tokens_for_user(user)
                return Response({
                    'token' : token,
                    'msg' : 'Login Successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "message" : "Email or Password is not valid"
                }, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response({
            'error' : serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    
#use profile view
class UserProfileView(APIView):
    renderer_classes =[UserRenderes]
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


#user change password view
class UserChangePasswordView(APIView):
    renderer_classes =[UserRenderes]
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        serializer = userChangePasswordSerializer(data=request.data, context = {'user' : request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg' : 'password change successfully'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

