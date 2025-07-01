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
# Nested router for branches under a restaurant
restaurant_router = routers.NestedDefaultRouter(router, 'restaurants', lookup = 'restaurant')
restaurant_router.register('branches', RestaurantBranchViewSet, basename='branche')

# Nested router for schedules, more-info, and contact-info under a branch
branch_router = routers.NestedDefaultRouter(restaurant_router, 'branches', lookup='branche')
branch_router.register('schedules', RestaurantScheduleViewSet, basename='schedule')
branch_router.register('more-info', MoreInfoViewSet, basename='branch-more-info')
branch_router.register('contact-info', ContactInfoViewSet, basename='branch-contact-info')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(restaurant_router.urls)),
    path('', include(branch_router.urls)),
]

