from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'price', 'size',
                  'color', 'created_at', 'created_by')
        read_only_fields = ['created_by']
        model = Item
