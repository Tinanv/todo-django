from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.tasks_list),
    path("tasks/<int:task_id>/", views.task_detail),
]
