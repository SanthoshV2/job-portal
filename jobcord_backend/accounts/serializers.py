from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type':'password'})

    class Meta:
        model=User
        fields= ('username','email','password','confirm_password','user_type' )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirm_password') #Remove confirm_password before creating user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type','job_seeker')
        )
        return user

    
