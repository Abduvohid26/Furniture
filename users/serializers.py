from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'user_roles',
            'password',
            'confirm_password'
        )

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if username and User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username already exists'})

        if password != confirm_password:
            raise ValidationError({'confirm_password': 'Passwords do not match'})

        return data

    def to_representation(self, instance):
        print('to_rep', instance)
        data = super(RegisterSerializer, self).to_representation(instance)
        data.update(instance.token())
        return data


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


