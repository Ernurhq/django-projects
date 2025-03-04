from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from django.http import HttpResponse

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {"customers": customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customers/detail.html", {"customer": customer})

def customer_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        Customer.objects.create(name=name, email=email)
        return redirect("customers-list")
    return render(request, "customers/create.html")
