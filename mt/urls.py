from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", include("customers.urls")),
    path("tables/", include("tables.urls")),
    path("reservations/", include("reservations.urls")),
    path("", lambda request: redirect("reservations:list")),  # Перенаправление на список бронирований
]

