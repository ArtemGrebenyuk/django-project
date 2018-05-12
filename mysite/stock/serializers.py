from rest_framework import serializers

from stock.models import Supplier


class SupplierSerializers(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='name')
    created_at = serializers.DateTimeField()
    payment_delay = serializers.IntegerField()
    enabled = serializers.BooleanField()

    class Meta:
        model = Supplier
        fields = ('supplier_name', 'created_at', 'payment_delay', 'enabled')



