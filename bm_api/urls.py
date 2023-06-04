from django.urls import path, include
from rest_framework import routers

from bm_api.views import PersonViewSet

router = routers.DefaultRouter()

router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('apis/', include('rest_framework.urls', namespace='rest_framework')),
]