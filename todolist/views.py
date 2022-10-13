from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url="/todolist/login/")
def set_status(request, id):
    item = Task.objects.get(user=request.user, id=id)
    item.is_finished = not item.is_finished
    item.save(update_fields=["is_finished"])
    return HttpResponseRedirect(reverse("todolist:show_todolist"))


@login_required(login_url="/todolist/login/")
def set_remove(request, id):
    item = Task.objects.get(user=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("todolist:show_todolist"))

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_item = Task.objects.filter(user=request.user)
    context = {"list_item": data_todolist_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'todolist.html',context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    data_todolist_item = Task.objects.filter(user=request.user)
    context = {"list_item": data_todolist_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'todolist_ajax.html',context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def new_task(request):
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        Task.objects.create(user = request.user,date = datetime.datetime.now(),title = request.POST.get('title'),description = request.POST.get('description'),)
        return response
    context = {"username": str(request.user).upper()}
    return render(request, 'new_task.html',context)

@login_required(login_url="/todolist/login/")
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def new_task_ajax(request):
    if request.method == "POST":
        response =  JsonResponse({"instance": "Task Created"},status=200)
        new_task = Task.objects.create(user = request.user,date = datetime.datetime.now(),title = request.POST.get('title'),description = request.POST.get('description'),)
        new_task.save()
        return response
    
