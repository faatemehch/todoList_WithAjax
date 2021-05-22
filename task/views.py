from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict


def task_list(request):
    tasks = Task.objects.filter( user=request.user ).all().order_by( 'date_added' )
    task_form = TaskForm( request.POST or None )

    if task_form.is_valid():
        new_task = task_form.save( commit=False )
        new_task.user = request.user
        new_task.save()
        # return redirect( request.path_info )
        return JsonResponse( {'task': model_to_dict( new_task )}, status=200 )

    context = {
        'tasks': tasks,
        'task_form': task_form
    }
    return render( request, 'task/task_list.html', context )


# @csrf_exempt
def delete_task(request, **kwargs):
    task = Task.objects.filter( user=request.user, id=kwargs['pk'] ).first()
    if task is not None:
        task.delete()
        return JsonResponse(
            {'msg': '***'}, safe=False )
    context = {
        'tasks': Task.objects.filter( user=request.user ).all().order_by( 'date_added' ),
        'task_form': TaskForm( request.POST or None )
    }
    return render( request, 'task/task_list.html', context )


def complete_task(request, **kwargs):
    task = Task.objects.filter( user=request.user, id=kwargs['pk'] ).first()
    if task is not None:
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        task.save()
        return JsonResponse( {'task': model_to_dict( task )}, status=200 )

    # context = {
    #     'tasks': Task.objects.filter( user=request.user ).all().order_by( 'date_added' ),
    #     'task_form': TaskForm( request.POST or None )
    # }
    # return render( request, 'task/task_list.html', context )
