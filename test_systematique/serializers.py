from rest_framework import serializers

from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'  # Include all fields by default

    def create(self, validated_data):
        test = Test.objects.create(**validated_data)
        test.analyser_robustesse()
        test.save()
        return test