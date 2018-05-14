from rest_framework import serializers

from stock.models import Supplier, Goods, Store


class SupplierSerializers(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='name')
    created_at = serializers.DateTimeField()
    payment_delay = serializers.IntegerField()
    enabled = serializers.BooleanField()

    class Meta:
        model = Supplier
        fields = ('supplier_name', 'created_at', 'payment_delay', 'enabled')


class GoodsSerializers(serializers.ModelSerializer):
    goods_name = serializers.CharField(source='name')
    description = serializers.CharField()
    gvls = serializers.BooleanField()
    supplier = serializers.CharField(source='Supplier.name')

    class Meta:
        model = Goods
        fields = ('goods_name', 'description', 'glvs', 'supplier')

class StoreSerializers(serializers.ModelSerializer):
    goods_name = serializers.CharField(source='Goods.name')
    is_present = serializers.BooleanField()
    amount = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    exp_date = serializers.DateTimeField()
    num_of_series = serializers.IntegerField()

    class Meta:
        model = Store
        fields = ('goods_name', 'is_present', 'amount', 'price', 'exp_date', 'num_of_series')






