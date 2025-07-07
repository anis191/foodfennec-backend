from django.urls import path,include
from rest_framework_nested import routers
from users.views import UserViewSet
from restaurants.views import *

# Main Router:
router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('districts', DistrictViewSet, basename='district')

# Main router (for Restaurants)
router.register('restaurants', RestaurantViewSet, basename='restaurant')
router.register('outlets', RestaurantOutletViewSet, basename='outlet')

# Nested router for schedules, more-info, and contact-info under a outlet
outlet_router = routers.NestedDefaultRouter(router, 'outlets', lookup='outlet')
outlet_router.register('schedules', OutletScheduleViewSet, basename='schedule')
outlet_router.register('more-info', MoreInfoViewSet, basename='outlet-more-info')
outlet_router.register('contact-info', ContactInfoViewSet, basename='outlet-contact-info')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(outlet_router.urls)),
]

