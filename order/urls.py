from django.urls import path, re_path, include
from rest_framework import routers

from order import viewsets


router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [
    path("", re_path, include(router.urls)),
]
