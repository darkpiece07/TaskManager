from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addTask/', views.addTask),
    path('getTask/<int:task_id>', views.getTask),
     path('allTasks/', views.allTasks),
]