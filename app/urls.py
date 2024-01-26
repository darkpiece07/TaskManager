from django.urls import path
from . import views
from .views import AllTasksView, AddTaskView, GetTaskView, DeleteTaskView, UpdateTaskView

urlpatterns = [
    path('login/', views.CustomAuthTokenLogin.as_view()),
    path('addTask/', AddTaskView.as_view()),
    path('getTask/<int:task_id>', GetTaskView.as_view()),
    path('allTasks/', AllTasksView.as_view()),
    path('deleteTask/<int:task_id>', DeleteTaskView.as_view()),
    path('updateTask/<int:task_id>', UpdateTaskView.as_view()),
]