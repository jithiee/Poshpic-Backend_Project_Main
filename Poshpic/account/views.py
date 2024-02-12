from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import( 
    RegisterSerializer ,
    LoginSerializer,
    ForgotPasswordSerializer,
    Userserializer ,
    VerifyAccountSerializer,
                        )
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from . models import User,Userprofile,PhotographerProfile
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from . email import sent_otp_vary_email
from rest_framework.generics import GenericAPIView



# this function used for jwt token generation 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterUserView(APIView):
    permissions_classes = [AllowAny]
    def post(self ,request , *args, **kwargs):
        print(request,'rrrrrrrrrrrrrrr')
        serializer = RegisterSerializer(data = request.data)
        print(request.data,'ddddddddddddddddddddd')
       
       
        if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    sent_otp_vary_email(serializer.data['email'])
                    return Response({'message':"register sucessfully check email "},status=status.HTTP_201_CREATED)
                                    
                    
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
 
# Assuming your PhotographerProfile model has a ForeignKey field named 'user'
class Verify_OTP(APIView):
    def post(self, request):
        serializer = VerifyAccountSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid email or OTP'}, status=status.HTTP_400_BAD_REQUEST)

            if user.otp != otp:
                return Response({'error': 'Incorrect OTP'}, status=status.HTTP_400_BAD_REQUEST)

            if not user.is_verified:
                user.is_verified = True
                if user.is_photographer:
                    # Assuming PhotographerProfile has a ForeignKey field named 'user'
                    PhotographerProfile.objects.create(user=user)
                else:
                    Userprofile.objects.create(user=user)
                user.save()
                return Response({'message': 'Account verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Account already verified'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        

# class LoginUserView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = LoginSerializer(data=request.data)
        
#         if serializer.is_valid(raise_exception=True):
#             email = serializer.validated_data['email']
#             password = serializer.validated_data['password']
            
            
            
#             user = authenticate(request=request, email=email, password=password  )
            
#             if user:
              
#                     token = get_tokens_for_user(user)
#                     print(token)
#                     return Response({"token":token})
                    
                  
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(request=request, email=email, password=password)
            
            if user:
                token = get_tokens_for_user(user)
                is_photographer = user.is_photographer if hasattr(user, 'is_photographer') else False
                return Response({"token": token, "isPhotographer": is_photographer})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
class ForgotpasswordView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():  
            email = serializer.validated_data.get('email')  
            print(email)
            try:
               
            
                user = User.objects.get(email = email)
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user) 

                reset_link = f"http://127.0.0.1:8000/resetpassword/{uidb64}/{token}/"
                subject = 'Forgot Password'
                message = f'Click the link to reset your password: {reset_link}'
                to_email = user.email
                send_mail(subject, message, None, [to_email])
                return Response({'msg': 'Password reset email sent successfully'}, status=status.HTTP_200_OK)
            
            except  User.DoesNotExist :
                return Response({"msg":"user is does not  exist"},status=status.HTTP_404_NOT_FOUND  ) 
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
                     
        
class ResetPasswordView(APIView):
        def put(self,request ,uidb64,token,*args,**kwargs):
            try:
                uid = urlsafe_base64_decode(uidb64).decode()
                user = User.objects.get(pk=uid)
            except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                user =None
                
                
            if user and default_token_generator.check_token(user, token):
               
                new_password = request.data.get('neww_password')
                confirm_password = request.data.get('confirm_password')

                if new_password == confirm_password:
              
                    user.set_password(new_password)
                    user.save() 
                    return Response({'detail': 'Password reset successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'new_password': 'This field is required.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'detail': 'Invalid reset link'}, status=status.HTTP_400_BAD_REQUEST)
            
  


# @authentication_classes([JWTAuthentication])  #its declire globaliyin setting.py  REST_FRAMEWORK
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = Userserializer(user)
        return Response(serializer.data)

    
    def patch(self,request, *args, **kwargs):
        try:
            userupdate = request.user
            serializer = Userserializer(userupdate ,data=request.data ,partial = True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response(serializer.data ,status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid data provided'},status=status.HTTP_404_NOT_FOUND)
        except  User.DoesNotExist:
            return Response({'msg': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response(
                {"msg":"server erorrrrr"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
   
class GetUserIdApivew(APIView):
    def get(self , request ,id ):
        user = User.objects.get(pk =id)
        serializer = Userserializer(user)
        return Response(serializer.data)
    
    
    
class PhtotgrapherApiview(APIView):
    def get(self, request ):
        user = User.objects.filter(photographerprofile__isnull = False)
        print(user, 'ooooooooooooooooooooooo')
        serilaizer = Userserializer(user , many = True)
        return Response(serilaizer.data,status=status.HTTP_200_OK )
        
        
        
    
        
            
    


    
                 
    
    

        
        
          
            
                
                
        

        


            
        
        
            
            
            
                
            

     
                  
                  
          
          
          
          
          
          
          
             
        
        
        
        
        
        
        
    
    
                    
            
        
            
            
        
