from django.urls import path
from . import views
from .views import ExampleClassBasedView

urlpatterns = [
    path('login/', views.CustomAuthTokenLogin.as_view()),
    path('addTask/', views.addTask),
    path('getTask/<int:task_id>', views.getTask),
    path('allTasks/', ExampleClassBasedView.as_view()),
    # path('allTasks/', views.allTasks),
    path('deleteTask/<int:task_id>', views.deleteTask),
    path('updateTask/<int:task_id>', views.updateTask),
]