from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user', 'name', 'description', 'category', 'image_url', 'created_at']
        read_only_fields = ['id', 'created_at', 'user', 'image_url']
