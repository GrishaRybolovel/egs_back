from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allows clients to set the page size using a query parameter
    max_page_size = 100  # Optional: maximum page size allowed