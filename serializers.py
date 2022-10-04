from rest_framework import serializers
from Prime.models import *

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'
