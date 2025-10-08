# work09/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.utils import timezone

def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'work09/todo_list.html', {'todos': todos})

def todo_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title:
            Todo.objects.create(title=title, due_date=due_date, created_at=timezone.now())
        return redirect('todo_list')
    return render(request, 'work09/todo_add.html')

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.due_date = request.POST.get('due_date')
        todo.is_completed = 'is_completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'work09/todo_edit.html', {'todo': todo})

def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('todo_list')
