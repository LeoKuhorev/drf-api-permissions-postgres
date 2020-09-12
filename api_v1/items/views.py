from rest_framework import generics

from items.models import Item
from .permissions import IsAuthorOrReadOnly
from .serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
