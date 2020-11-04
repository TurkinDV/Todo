from django.db import models

class ToDoList(models.Model):
    task = models.CharField(max_length=200)