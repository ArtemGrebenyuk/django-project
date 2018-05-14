from django.shortcuts import render, render_to_response

from rest_framework.viewsets import ModelViewSet

# Create your views here.
from stock.models import Supplier
from stock.serializers import SupplierSerializers


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers



