from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
from django.forms.models import model_to_dict


@login_required( login_url='login' )
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


@login_required( login_url='login' )
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


@login_required( login_url='login' )
def complete_task(request, **kwargs):
    task = Task.objects.filter( user=request.user, id=kwargs['pk'] ).first()
    if task is not None:
        if task.completed:
            task.completed = False
        else:
            task.completed = True
        task.save()
        return JsonResponse( {'task': model_to_dict( task )}, status=200 )

    context = {
        'tasks': Task.objects.filter( user=request.user ).all().order_by( 'date_added' ),
        'task_form': TaskForm( request.POST or None )
    }
    return render( request, 'task/task_list.html', context )


class CostumeLoginView( LoginView ):
    fields = '__all__'
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy( 'task_list' )

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect( 'login/' )
        return super( CostumeLoginView, self ).get( *args, **kwargs )


class RegisterView( FormView ):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy( 'task_list' )

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect( 'task_list' )
        return super( RegisterView, self ).get( *args, **kwargs )

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login( self.request, user )
        return super( RegisterView, self ).form_valid( form )
