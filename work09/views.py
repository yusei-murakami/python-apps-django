from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from datetime import date

#　ToDo一覧表示
def todo_list(request):
    filter_value = request.GET.get('filter', 'all')
    today = date.today()

    if filter_value == 'completed':
        todos = Todo.objects.filter(is_completed=True).order_by('due_date')
    elif filter_value == 'pending':
        todos = Todo.objects.filter(is_completed=False).order_by('due_date')
    else:
        todos = Todo.objects.all().order_by('due_date')

    context = {
        'todos': todos,
        'filter': filter_value,
        'today': today,
    }
    return render(request, 'work09/todo_list.html', context)


#　ToDo新規作成
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('work09:list')
    else:
        form = TodoForm()
    return render(request, 'work09/todo_form.html', {'form': form, 'title': '新しいタスクを追加'})


#　ToDo編集
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('work09:list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'work09/todo_form.html', {'form': form, 'title': 'タスクを編集'})


#　ToDo削除
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('work09:list')
    return render(request, 'work09/todo_confirm_delete.html', {'todo': todo})


#　完了状態トグル
def toggle_complete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('work09:list')

