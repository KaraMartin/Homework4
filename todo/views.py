from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {'tasks': ['foo', 'bar', 'baz']}
    return render(request, 'todo/index.html', context)

def update(request):
    return render(request, 'todo/update.html')

def delete(request):
    return render(request, 'todo/delete.html')