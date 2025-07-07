from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import RestaurantFilter
from rest_framework.decorators import action
from rest_framework.response import Response

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.annotate(total_restaurants=Count('available_outlets')).all()
    serializer_class = DistrictSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = RestaurantFilter

class RestaurantOutletViewSet(ModelViewSet):
    queryset = RestaurantOutlet.objects.all()
    # serializer_class = RestaurantOutletSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        restaurant_id = validated_data['restaurant'].id
        if not RestaurantOutlet.objects.filter(restaurant=restaurant_id).exists():
            serializer.save(is_main = True)
        else:
            serializer.save()
    
    @action(detail=True, methods=['put'])
    def set_as_main(self, request, pk=None):
        outlet = self.get_object()
        restaurant = outlet.restaurant
        RestaurantOutlet.objects.filter(restaurant=restaurant, is_main=True).update(is_main=False)
        outlet.is_main = True
        outlet.save()
        return Response({'message': 'This outlet is now set as the main outlet!'})
    
    def get_serializer_class(self):
        if self.action == 'set_as_main':
            return EmptySerializers
        return RestaurantOutletSerializer

class OutletScheduleViewSet(ModelViewSet):
    # queryset = RestaurantSchedule.objects.all()
    def get_queryset(self):
        return OutletSchedule.objects.filter(
            restaurant_outlet_id = self.kwargs.get('outlet_pk')
        )
    serializer_class = OutletScheduleSerializer

class MoreInfoViewSet(ModelViewSet):
    # queryset = MoreInfo.objects.all()
    def get_queryset(self):
        return MoreInfo.objects.filter(
            restaurant_outlet_id = self.kwargs.get('outlet_pk'),
            # restaurant_outlet__restaurant_id = self.kwargs.get('restaurant_pk')
        )
    
    serializer_class = MoreInfoSerializer

class ContactInfoViewSet(ModelViewSet):
    # queryset = ContactInfo.objects.all()
    def get_queryset(self):
        return ContactInfo.objects.filter(
            restaurant_outlet_id = self.kwargs.get('outlet_pk'),
            # restaurant_branch__restaurant_id = self.kwargs.get('restaurant_pk')
        )
    serializer_class = ContactInfoSerializer

