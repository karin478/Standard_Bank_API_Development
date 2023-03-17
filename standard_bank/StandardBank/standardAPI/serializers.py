from rest_framework import serializers
from .models import User, AppUsage, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AppUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsage
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'