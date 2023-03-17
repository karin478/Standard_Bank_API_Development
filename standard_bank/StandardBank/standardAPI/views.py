from django.shortcuts import render
from rest_framework import generics
from .models import User, AppUsage, Transaction
from .serializers import UserSerializer, AppUsageSerializer, TransactionSerializer
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

class AppUsageViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = AppUsage.objects.all()
    serializer_class = AppUsageSerializer

class UserViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TransactionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer




class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AppUsageList(generics.ListCreateAPIView):
    queryset = AppUsage.objects.all()
    serializer_class = AppUsageSerializer



class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer





