from django.shortcuts import render, redirect
from .models import Todo
from .forms import TdodForms
from django.contrib import messages

def index(request):
    todos = Todo.objects.filter(title__contains = request.GET.get('search', ''))
    return render(request, 'todo/index.html', {
            'todos': todos
        })


def view(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'todo/detail.html', {
        'todo': todo
    })

def edit(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'GET':
        form = TdodForms(instance=todo)
        return render(request, 'todo/edit.html', {
            'form': form,
            'id': id
        })
    
    if(request.method == 'POST'):
        form = TdodForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        messages.success(request, "Tarea actualizada")
        return render(request, 'todo/edit.html', {
            'form' : form,
            'id' : id
            })

def create(request):
    if request.method == 'GET':
        form = TdodForms()
        return render(request, 'todo/create.html', {
            'form': form
        })
    if request.method == 'POST':
        form = TdodForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('todo')
