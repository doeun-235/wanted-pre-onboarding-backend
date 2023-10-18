from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Item

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer