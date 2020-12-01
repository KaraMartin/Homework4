from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def update(request):
    return HttpResponse("Update Page")

def delete(request):
    return HttpResponse("Delete Page")