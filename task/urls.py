from django.urls import path

from todoList_WithAjax import settings
from .views import task_list, delete_task, complete_task, CostumeLoginView, RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path( '', task_list, name='task_list' ),
    path( 'delete_task/<int:pk>', delete_task, name='delete_task' ),
    path( 'complete_task/<int:pk>', complete_task, name='complete_task' ),
    path( 'login/', CostumeLoginView.as_view(), name='login' ),
    path( 'register/', RegisterView.as_view(), name='register' ),
    path( 'logout/', LogoutView.as_view( next_page='login' ), name='logout' ),
]
