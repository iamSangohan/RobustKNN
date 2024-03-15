from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('test', TestViewSet)  # Use descriptive names for clarity

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs at the root path
]