from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    context = {}
    return render(request, 'app/index.html', context)


# Create a task
@csrf_exempt
def addTask(request):
    data = {'success' : False, 'message': "Your task is added to the all Tasks!"}
    if request.method == "POST":
        title = request.POST.get("title")
        task = Task.objects.filter(title = title)
        # checking for duplicate task!
        if task.exists():
            data = {'success' : False, 'message': "Task exists with the same name!"}
            print("task exists in the database.")
            return JsonResponse({"data": data})
        
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        task = Task(title = title, description = description, due_date = due_date)
        task.save()
        data = {
            "success": True,
            "id" : task.id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status
        }

    return JsonResponse({"data": data})

