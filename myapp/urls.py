from django.urls import path
from django.urls import path, include
from rest_framework import routers
from .views import AssistantViewSet

router = routers.DefaultRouter()
router.register(r'assistants', AssistantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
