from rest_framework import viewsets
from .serializers import *


class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.object.all()
    serializers = MarkaSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.object.all()
    serializers = CarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.object.all()
    serializers = CarSerializer


class CarPhotosViewSet(viewsets.ModelViewSet):
    queryset = CarPhotos.object.all()
    serializers = CarPhotosSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.object.all()
    serializers = RatingSerializer
