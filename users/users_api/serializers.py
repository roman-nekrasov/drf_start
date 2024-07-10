from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'country', 'desiredSalary', 'grade', 'exp', 'technologies']


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name', 'country', 'desiredSalary', 'grade', 'exp', 'technologies']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            country=validated_data['country'],
            desiredSalary=validated_data['desiredSalary'],
            grade=validated_data['grade'],
            exp=validated_data['exp'],
            technologies=validated_data['technologies'],
        )
        return user


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return {
                'email': user.email,
                'token': str(RefreshToken.for_user(user).access_token)
            }
        raise serializers.ValidationError("Incorrect email and/or password")
