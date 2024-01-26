from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

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
        status = request.POST.get("status")
        print(status)
        task = Task(title = title, description = description, due_date = due_date, status = status)
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



# Need to apply authentication on all APIs
# Get a single task by task_id
def getTask(request, task_id):
    try:
        task = Task.objects.get(id = task_id)
        task_data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date,
            "status": task.status
        }
        return JsonResponse({"task": task_data}, status=200)
    
    except Task.DoesNotExist:
        return JsonResponse({"data": "task id does not exist!"}, status = 404)
    


# List all tasks
def allTasks(request):
    tasks = Task.objects.all()
    task_list = [{'id': task.id, 'title': task.title, 'description': task.description, 'due_date': task.due_date, 'status': task.status} for task in tasks]
    return JsonResponse({"tasks": task_list})




# Delete a single task by task_id
def deleteTask(request, task_id):
    try:
        task = Task.objects.get(id = task_id)
        task.delete()
        return JsonResponse({"message": "Task deleted!"})
    
    except Task.DoesNotExist:
        return JsonResponse({"message": "Task does not exist, provide an existing task id."})
    


# Update an existing Task with its id provided
@csrf_exempt
def updateTask(request, task_id):
    data = {'success': False, 'message': "Failed to update task."}

    if request.method == "POST":
        try:
            task = Task.objects.get(id=task_id)

            title = request.POST.get("title")
            description = request.POST.get("description")
            due_date = request.POST.get("due_date")
            status = request.POST.get("status")
            
            if title:
                task.title = title
            if description:
                task.description = description

            if due_date:
                task.due_date = timezone.datetime.strptime(due_date, '%Y-%m-%d').date()

            if status:
                task.status = status
            task.save()
            data = {
                "success": True,
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "status": task.status,
                "message": "Task updated successfully."
            }
        except Task.DoesNotExist:
            data['message'] = f"Task with ID {task_id} does not exist."
        except Exception as e:
            data['message'] = f"Error: {str(e)}"

    return JsonResponse({"data": data})