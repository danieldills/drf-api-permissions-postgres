from django.db.models import fields
from rest_framework import serializers
from .models import Groceries

class GroceriesSerializer(serializers.ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Groceries
