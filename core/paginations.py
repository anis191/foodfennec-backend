from rest_framework.pagination import PageNumberPagination

class OutletsPagination(PageNumberPagination):
    page_size = 10