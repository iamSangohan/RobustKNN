from django.shortcuts import render
from rest_framework import viewsets

from test_systematique.models import Test
from test_systematique.serializers import TestSerializer

# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
    
    queryset = Test.objects.all()
    serializer_class = TestSerializer