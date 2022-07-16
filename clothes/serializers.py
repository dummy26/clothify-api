from rest_framework import serializers
from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):

    size = serializers.CharField(source='get_size_display')  # Make it read_only if POST should send 'M', 'W' or 'O'
    gender = serializers.CharField(source='get_gender_display')
    color = serializers.CharField(source='get_color_display')
    category = serializers.CharField(source='get_category_display')

    class Meta:
        model = Cloth
        fields = ('name', 'description', 'retail_price', 'sell_price', 'size', 'gender', 'color', 'category')
