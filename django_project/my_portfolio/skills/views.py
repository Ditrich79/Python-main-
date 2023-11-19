from django.shortcuts import render, redirect, get_object_or_404
from .models import Skills
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import TodoSerializer, SkillsSerializer


def home(request):
    return render(request, 'skills/home.html')


@login_required
def index(request):
    projects = Skills.objects.all()
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'skills/index.html', {'projects': projects, 'todos': todos})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Такое имя пользователя уже существует, задайте другое'})
        else:
            return render(request, 'skills/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпадают'})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {'form': AuthenticationForm(),
                                                             'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'skills/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('index')
        except ValueError:
            return render(request, 'skills/createtodo.html', {'form': TodoForm(),
                                                              'error': 'Переданы неверные данные. Попробуйте ещё раз.'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'skills/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('index')
        except ValueError:
            return render(request, 'skills/viewtodo.html', {
                'todo': todo,
                'form': form,
                'error': 'Неверные данные'
            })


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('index')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'skills/completedtodos.html', {'todos': todos})


class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class SkillsAPIView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
