from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to my Django Project!</h1>")
