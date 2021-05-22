from django.urls import path
from .views import task_list, delete_task, complete_task

urlpatterns = [
    path( '', task_list, name='task_list' ),
    path( 'delete_task/<int:pk>' , delete_task, name = 'delete_task' ),
    path( 'complete_task/<int:pk>' , complete_task, name = 'complete_task' ),
]
