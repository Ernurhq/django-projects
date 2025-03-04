from django.urls import path
from .views import (
    ReservationListView,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
)

app_name = "reservations"

urlpatterns = [
    path("", ReservationListView.as_view(), name="list"),
    path("create/", ReservationCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ReservationUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ReservationDeleteView.as_view(), name="delete"),
]
from django.urls import path
from .views import ReservationListView

app_name = "reservations"

urlpatterns = [
    path("", ReservationListView.as_view(), name="list"),  # Главная страница для бронирований
]
from django.urls import path
from .views import ReservationListView, ReservationCreateView

app_name = "reservations"  # <-- Добавляем app_name, важно!

urlpatterns = [
    path("", ReservationListView.as_view(), name="list"),
    path("create/", ReservationCreateView.as_view(), name="create"),  # <-- Имя "create"
]
