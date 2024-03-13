from django.urls import path, include
from rest_framework import routers

# from .viewsets.order_viewset import OrderViewSet

from order import viewsets

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]
