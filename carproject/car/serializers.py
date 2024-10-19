from rest_framework import serializers
from .models import *


class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotos
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
