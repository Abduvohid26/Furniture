from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'user_roles',
            'password',

        )

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        username = data.get('username')

        if username and User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username already exists'})

        return data

    # def to_representation(self, instance):
    #     data = super(RegisterSerializer, self).to_representation(instance)
    #     tokens = instance.token()
    #     data.update(tokens)
    #     return data


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password'
        ]


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'user_roles', 'created_at')



