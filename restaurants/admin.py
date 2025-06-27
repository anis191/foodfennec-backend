from django.contrib import admin
from restaurants.models import *

# admin.site.register(District)
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_code', 'created_at')
    search_fields = ('name', 'district_code')

# admin.site.register(Restaurant)
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

class MoreInfoInline(admin.StackedInline):
    model = MoreInfo
    extra = 0

class ContactInfoInline(admin.StackedInline):
    model = ContactInfo
    extra = 0

# admin.site.register(RestaurantBranch)
@admin.register(RestaurantBranch)
class RestaurantBranchAdmin(admin.ModelAdmin):
    list_display = ('branch_code', 'restaurant', 'district', 'city', 'location')
    search_fields = ('branch_code', 'restaurant__name', 'district__name')
    list_filter = ('district',)
    inlines = [MoreInfoInline, ContactInfoInline]

# admin.site.register(MoreInfo)
# admin.site.register(ContactInfo)

# admin.site.register(RestaurantSchedule)
@admin.register(RestaurantSchedule)
class RestaurantScheduleAdmin(admin.ModelAdmin):
    list_display = ('restaurant_branch', 'day', 'opening_time', 'closing_time')
    list_filter = ('day', 'restaurant_branch')
