from django.urls import path
from .views import *

urlpatterns = [

    path('', MarkaListViewSet.as_view({'get': 'list', 'post': 'create'}), name='marka_list'),
    path('<int:pk>/', MarkaDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='marka_detail'),

    path('users/', CarModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-model_list'),
    path('users/<int:pk>/', CarModelViewSet.as_view({f'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='car-model_detail'),

    path( 'category/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('category/<int:pk>/', CarViewSet.as_view({f'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='car_detail'),

    path('rating/', CarPhotosViewSet.as_view({'get': 'List', 'post': 'create'}), name='photos_list'),
    path(' rating/<int:pk>/', CarPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='photos_detail'),
]

