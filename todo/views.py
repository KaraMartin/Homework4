from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def update(request):
    return HttpResponse("Update Page")

def delete(request):
    return HttpResponse("Delete Page")