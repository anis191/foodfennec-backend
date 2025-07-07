from django_filters.rest_framework import FilterSet
from restaurants.models import Restaurant

class RestaurantFilter(FilterSet):
    class Meta:
        model = Restaurant
        fields = {
            # 'branches__district_id' : ['exact'],
            # 'price' : ['gt','lt']
        }