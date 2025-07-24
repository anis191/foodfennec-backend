from rest_framework import serializers
from .models import *
from django.db.models import Count

class EmptySerializers(serializers.Serializer):
    pass

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','description','owner','logo']

class OutletScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletSchedule
        fields = ['id','restaurant_outlet','day','opening_time','closing_time']

class RestaurantOutletSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(
        queryset = Restaurant.objects.all(), write_only=True
    )
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    district = serializers.PrimaryKeyRelatedField(
        queryset = District.objects.all(), write_only=True
    )
    district_name = serializers.CharField(source='district.name',read_only=True)
    delivery_fee = serializers.DecimalField(source='info.delivery_fee', max_digits=6, decimal_places=2, read_only=True)
    delivery_time = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = RestaurantOutlet
        fields = ['id','restaurant','restaurant_name','district','district_name','city','location','is_main','delivery_fee','delivery_time']
    
    def get_delivery_time(self, obj):
        if hasattr(obj, 'info') and obj.info is not None:
            return f"{obj.info.delivery_time_min}-{obj.info.delivery_time_max} mins"
        return None

class DistrictSerializer(serializers.ModelSerializer):
    total_restaurants = serializers.IntegerField(read_only=True)
    class Meta:
        model = District
        fields = ['id','name','district_code','total_restaurants']

class MoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInfo
        fields = ['id','restaurant_outlet','delivery_fee','minimum_order','offer_text','delivery_time']

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id','restaurant_outlet','phone_number','email','whatsapp_number','facebook_page','website','map_location_url']

