from rest_framework.pagination import PageNumberPagination
# ============================================================================ #



# ============================ PROPERTY PAGINATION =========================== #


class PropertyPagination(PageNumberPagination):
    page_size = 3