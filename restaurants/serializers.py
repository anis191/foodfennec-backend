from rest_framework import serializers
from .models import *

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id','name','district_code']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','description','owner']

class RestaurantBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantBranch
        fields = ['id','restaurant','district','city','location']

class RestaurantScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantSchedule
        fields = ['id','restaurant_branch','day','opening_time','closing_time']

class MoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInfo
        fields = ['id','restaurant_branch','delivery_fee','minimum_order','offer_text','delivery_time']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id','restaurant_branch','phone_number','email','whatsapp_number','facebook_page','website','map_location_url']
