from django.contrib.auth.models import User
from django.db import models


class Task( models.Model ):
    user = models.ForeignKey( User, on_delete=models.CASCADE, blank=True, null=True )
    task_title = models.CharField( max_length=150 )
    date_added = models.DateField( auto_now_add=True )
    completed = models.BooleanField( default=False )

    def __str__(self):
        return self.task_title
