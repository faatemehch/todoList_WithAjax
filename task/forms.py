from django import forms
from .models import Task


class TaskForm( forms.ModelForm ):
    class Meta:
        model = Task
        fields = ['task_title']

        widgets = {
            'task_title': forms.TextInput(
                attrs={'type': 'text', 'placeholder': 'Create Task', 'class': 'form-control mr-sm-2'} ),
        }
