from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Reservation
from .forms import ReservationForm

class ReservationListView(View):
    def get(self, request):
        reservations = Reservation.objects.all()
        return render(request, "reservations/list.html", {"reservations": reservations})

class ReservationCreateView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, "reservations/create.html", {"form": form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reservations:list")
        return render(request, "reservations/create.html", {"form": form})

class ReservationUpdateView(View):
    def get(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        form = ReservationForm(instance=reservation)
        return render(request, "reservations/update.html", {"form": form})

    def post(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservations:list")
        return render(request, "reservations/update.html", {"form": form})

class ReservationDeleteView(View):
    def get(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        return render(request, "reservations/delete.html", {"reservation": reservation})

    def post(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.delete()
        return redirect("reservations:list")
from django.shortcuts import render
from django.views import View

class ReservationListView(View):
    def get(self, request):
        return render(request, "reservations/list.html")
