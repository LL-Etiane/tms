from rest_framework import serializers 
from users.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id','name']