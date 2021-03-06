from rest_framework import viewsets
from API.serializers import ShopSerializer, ProductSerializer, ContactSerializer
from shop.models import *

class ShopViewSet(viewsets.ModelViewSet):
    
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
