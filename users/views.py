from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from users.models import User

from .serializers import UserCreateSerializer, UserViewializer


class UserCreateView(APIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    # def get(self, request):
    #     if not request.user.is_authenticated:
    #             return Response(status=status.HTTP_401_UNAUTHORIZED)
    #     serializer = self.serializer_class(request.user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserView(APIView):
    serializer_class = UserViewializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(pk=request.user.id)

            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "User not found"})
