from django.shortcuts import render, render_to_response

from rest_framework.viewsets import ModelViewSet

# Create your views here.
from stock.models import Goods, Supplier, Store
from stock.serializers import SupplierSerializers, GoodsSerializers, StoreSerializers


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers


class GoodsViewSet(ModelViewSet):
    queryset = Goods.object.all()
    serializer_class = GoodsSerializers


class StoreViewSet(ModelViewSet):
    queryset = Store.object.all()
    serializer_class = StoreSerializers




