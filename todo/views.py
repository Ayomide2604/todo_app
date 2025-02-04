from django.shortcuts import render,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Todo

# Create your views here.


def home(request):

    return render(request, 'todo/home.html')


@login_required
def todos(request):

    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    context = {'todos': todos}
    return render(request, 'todo/todos.html', context)


def add_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        if task.strip() == "":
            return None  
        user = request.user
        Todo.objects.create(user=user, task=task)

    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    context = {'todos': todos}
    return render(request, 'todo/todos.html', context)


def edit_todo(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=pk, user=request.user)
        todo.is_completed = not todo.is_completed
        todo.save()

    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    context = {'todos': todos}
    return render(request, 'partials/todo_list.html', context)


def delete_todo(request, pk):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=pk, user=request.user)
        todo.delete()

    todos = Todo.objects.filter(user=request.user).order_by('created_at')
    context = {'todos': todos}
    return render(request, 'partials/todo_list.html', context)
