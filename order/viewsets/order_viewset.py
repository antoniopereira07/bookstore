from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication #added
from rest_framework.permissions import IsAuthenticated #added

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
  authentication_classes = [
    SessionAuthentication, # added
    BasicAuthentication, # added
    TokenAuthentication, # added
  ] 
  permission_classes = [IsAuthenticated]  # added 
  
  serializer_class = OrderSerializer
  queryset = Order.objects.all().order_by('id')
