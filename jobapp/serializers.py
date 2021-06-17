from rest_framework import serializers
from .models import Jobs


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Jobs
