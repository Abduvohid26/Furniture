from django.contrib.auth import authenticate, logout
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import User


class SignUpView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class LoginApiView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response(
                {
                    'id': user.id,
                    'access_token': user.token()['access_token'],
                    'refresh_token': user.token()['refresh_token'],
                    'username': user.username,
                    'roles': user.user_roles,
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'success': False,
                    'message': 'username or password invalid'
                }, status=status.HTTP_401_UNAUTHORIZED
            )


class UsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('-created_at')
    permission_classes = [permissions.AllowAny]


class UsersDetailView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = get_object_or_404(User, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                }
            )
        else:
            user.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'User successfully deleted'
                }, status=status.HTTP_200_OK
            )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"}, status=status.HTTP_200_OK)
