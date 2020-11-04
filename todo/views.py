from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import TaskForms

def index(request):
    tasks = ToDoList.objects.all()

    if request.method == 'POST':
        form = TaskForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = TaskForms()
    
    return render(request, 'todo/index.html', {'form':form,'tasks':tasks})

def remove(request, pk):
    task = ToDoList.objects.get(id=pk)
    task.delete()
    return redirect('/')