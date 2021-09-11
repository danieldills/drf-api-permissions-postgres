from rest_framework import generics
from .serializers import GroceriesSerializer
from .models import Groceries
from .permissions import IsOwnerOrReadOnly

class GroceriesList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Groceries.objects.all()
  serializer_class = GroceriesSerializer

class GroceriesDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Groceries.objects.all()
  serializer_class = GroceriesSerializer
  
