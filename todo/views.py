from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Task
import json

@csrf_exempt
def tasks_list(request):
    if request.method == "GET":
        tasks = Task.objects.all().values()
        return JsonResponse(list(tasks), safe=False)

    if request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get("title"),
            start_date=parse_date(data.get("start_date")),
            end_date=parse_date(data.get("end_date"))
        )
        return JsonResponse({"message": "Task created", "id": task.id})
    

@csrf_exempt
def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        task.title = data.get("title", task.title)
        task.start_date = parse_date(data.get("start_date")) or task.start_date
        task.end_date = parse_date(data.get("end_date")) or task.end_date
        task.save()
        return JsonResponse({"message": "Task updated"})

    if request.method == "DELETE":
        task.delete()
        return JsonResponse({"message": "Task deleted"})

    if request.method == "GET":
        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "start_date": task.start_date,
            "end_date": task.end_date
        })

