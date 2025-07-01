from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantBranchViewSet(ModelViewSet):
    queryset = RestaurantBranch.objects.all()
    serializer_class = RestaurantBranchSerializer

class RestaurantScheduleViewSet(ModelViewSet):
    queryset = RestaurantSchedule.objects.all()
    serializer_class = RestaurantScheduleSerializer

class MoreInfoViewSet(ModelViewSet):
    queryset = MoreInfo.objects.all()
    serializer_class = MoreInfoSerializer

class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

