from urllib import request
from rest_framework import serializers
from .models import Item

class PostSerializer(serializers.ModelSerializer):
    item_pic = serializers.ImageField(use_url=True)

    class Meta:
        model = Item
        fields = '__all__'


