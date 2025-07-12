from rest_framework import serializers
from .models import Purchase
from apps.items.serializers import ItemSerializer

class PurchaseSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = Purchase
        fields = ['id', 'item', 'status', 'purchased_at']
        read_only_fields = ['id', 'purchased_at']