from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import UserSerializer


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer