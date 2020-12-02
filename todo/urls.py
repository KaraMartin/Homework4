from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
    path('add', views.add, name="add")
]