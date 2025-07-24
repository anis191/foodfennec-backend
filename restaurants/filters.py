from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter
from restaurants.models import Restaurant, RestaurantOutlet
from django.db.models import Q

class RestaurantOutletFilter(FilterSet):
    class Meta:
        model = RestaurantOutlet
        fields = {
            'district_id' : ['exact'],
            'city' : ['icontains'],
            'location' : ['icontains'],
            'restaurant__name' : ['icontains'],
            'info__delivery_time_max' : ['lte']
        }
    