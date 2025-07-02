from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','description','owner']

class RestaurantScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantSchedule
        fields = ['id','restaurant_branch','day','opening_time','closing_time']

'''
class RestaurantBranchSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset = Restaurant.objects.all(), write_only=True
    )
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    district = serializers.PrimaryKeyRelatedField(
        queryset = District.objects.all(), write_only=True
    )
    district_name = serializers.CharField(source='district.name',read_only=True)
    # It's a related field:
    schedules = RestaurantScheduleSerializer(many=True, read_only=True)
    more_info = MoreInfoSerializer(read_only=True, source='info')
    contact_info = ContactInfoSerializer(read_only=True)
    class Meta:
        model = RestaurantBranch
        fields = ['id','restaurant','restaurant_name','district','district_name','city','location','schedules','more_info','contact_info']
'''

class RestaurantBranchSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset = Restaurant.objects.all(), write_only=True
    )
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    district = serializers.PrimaryKeyRelatedField(
        queryset = District.objects.all(), write_only=True
    )
    district_name = serializers.CharField(source='district.name',read_only=True)
    class Meta:
        model = RestaurantBranch
        fields = ['id','restaurant','restaurant_name','district','district_name','city','location']

class DistrictSerializer(serializers.ModelSerializer):
    total_restaurants = serializers.IntegerField(read_only=True)
    class Meta:
        model = District
        fields = ['id','name','district_code','total_restaurants']

class MoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInfo
        fields = ['id','restaurant_branch','delivery_fee','minimum_order','offer_text','delivery_time']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id','restaurant_branch','phone_number','email','whatsapp_number','facebook_page','website','map_location_url']
