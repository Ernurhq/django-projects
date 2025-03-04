from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Table

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/list.html', {'tables': tables})

def table_detail(request, id):
    table = get_object_or_404(Table, id=id)
    return render(request, 'tables/detail.html', {'table': table})

def create_table(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        seats = request.POST.get('seats')
        table = Table.objects.create(number=number, seats=seats)
        return JsonResponse({'message': 'Столик создан', 'id': table.id})
    return render(request, 'tables/create.html')

def table_create(request):
    return render(request, 'tables/table_form.html')


def available_tables(request):
    return render(request, "tables/available_tables.html")