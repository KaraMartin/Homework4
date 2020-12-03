from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
    path('complete_task', views.complete_task, name="complete_task"),
    path('add', views.add, name="add")
]
