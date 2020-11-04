from django.shortcuts import render
from .models import ToDoList

def index(request):
    tasks = ToDoList.objects.all()
    return render(request, 'todo/index.html', {'tasks':tasks})
