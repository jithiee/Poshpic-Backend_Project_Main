from rest_framework import serializers
from .models import User, Userprofile, PhotographerProfile
import re  


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = [
        
            "username",
            "email",
            "is_photographer",
            "is_user",
            "password",
            "confirm_password",
            "is_verified",
            "otp",
        ]

  

    def validate(self, attrs):
        if attrs['password'] != attrs ['confirm_password']:
            raise serializers.ValidationError({'msg':'Invalid password , passwords  are not same '})
        return attrs



    def create(self, validated_data):
        validated_data.pop(
            "confirm_password", None
        )  # pop is dict method None is default , confirm_password don't want to store in database

        user = User.objects.create_user(  # create_user usring for hashing the password
            **validated_data
        )
        return user


# OTP verification 
class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()

#  Resent OTP 
class ResentOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
   



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ["city", "phone", "country", "address", "profile_image"]

  

    
class PhotogrpherProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = PhotographerProfile
        fields = [
            "user_id",
            "specialty",
            "experience",
            "city",
            "status",
            "address",
            "phone",
            "profile_image",
            "amount",
        ]



class Userserializer(serializers.ModelSerializer):
    userData = UserProfileSerializer(source="userprofile", required=False)
    PhotographerData = PhotogrpherProfileSerializer(
        source="photographerprofile", required=False
    )

    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "userData",
            "PhotographerData",
        )

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()

        userprofile_data = validated_data.pop("userprofile", {})
        if userprofile_data:
            userprofile_instance, created = Userprofile.objects.get_or_create(
                user=instance
            )

            for attr, value in userprofile_data.items():
                setattr(userprofile_instance, attr, value)

            userprofile_instance.save()

        photographer_data = validated_data.pop("photographerprofile", {})
        if photographer_data:
            photographer_instance, created = PhotographerProfile.objects.get_or_create(
                user=instance
            )

            for attr, value in photographer_data.items():
                setattr(photographer_instance, attr, value)

            photographer_instance.save()

        return instance
    