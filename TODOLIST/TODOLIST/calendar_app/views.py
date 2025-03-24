from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, TaskForm
from .models import Task
from .forms import TaskForm 

def index(request):
    return render(request, 'calendar_app/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'calendar_app/signup.html', {'form': form})

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'calendar_app/dashboard.html', {'tasks': tasks, 'form': form})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        task.delete()
    return redirect('dashboard')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.completed = request.POST.get('completed') == 'on' #get the completed value from the form
            task.save()
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = TaskForm(instance=task)
    return render(request, 'calendar_app/edit_task.html', {'form': form, 'task': task})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('dashboard')
