from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from django.db.models import Count

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.annotate(total_restaurants=Count('restaurants')).all()
    serializer_class = DistrictSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantBranchViewSet(ModelViewSet):
    # queryset = RestaurantBranch.objects.all()
    serializer_class = RestaurantBranchSerializer
    def get_queryset(self):
        return RestaurantBranch.objects.filter(
            restaurant_id = self.kwargs.get('restaurant_pk')
        )
    

class RestaurantScheduleViewSet(ModelViewSet):
    # queryset = RestaurantSchedule.objects.all()
    def get_queryset(self):
        return RestaurantSchedule.objects.filter(
            restaurant_branch_id = self.kwargs.get('branch_pk')
        )
    serializer_class = RestaurantScheduleSerializer

class MoreInfoViewSet(ModelViewSet):
    # queryset = MoreInfo.objects.all()
    def get_queryset(self):
        return MoreInfo.objects.filter(
            restaurant_branch_id = self.kwargs.get('branch_pk'),
            restaurant_branch__restaurant_id = self.kwargs.get('restaurant_pk')
        )
    
    serializer_class = MoreInfoSerializer

class ContactInfoViewSet(ModelViewSet):
    # queryset = ContactInfo.objects.all()
    def get_queryset(self):
        return ContactInfo.objects.filter(
            restaurant_branch_id = self.kwargs.get('branch_pk'),
            restaurant_branch__restaurant_id = self.kwargs.get('restaurant_pk')
        )
    serializer_class = ContactInfoSerializer

