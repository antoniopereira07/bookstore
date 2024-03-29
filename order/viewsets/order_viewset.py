from rest_framework.viewsets import ModelViewSet

from order.models.order import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")