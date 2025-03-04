from django.urls import path
from .views import table_list, table_create, available_tables

urlpatterns = [
    path("", table_list, name="tables-list"),
    path("create/", table_create, name="tables-create"),
    path("available/", available_tables, name="tables-available"),
]
