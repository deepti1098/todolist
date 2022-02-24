import re
from telnetlib import STATUS
from django.shortcuts import render, redirect,HttpResponse
from .models import ToDO
from User.models import User_detail


def todoView(request):
    if not request.user.is_authenticated:
        return redirect("login/")
    user = User_detail.objects.get(user=request.user)
    ls = ToDO.objects.filter(user=user)
    for i in ls:
        i.date = i.date.strftime("%Y-%m-%dT%H:%M:%S") 
    context = {'todolist': ls}
    return render(request, 'list.html', context)


def addtaskview(request):
    user = User_detail.objects.get(user=request.user)
    if request.method == "POST":
        Title = request.POST["titl"]
        Desc = request.POST["descr"]
        Date = request.POST["datetime"]
        ToDO.objects.create(user=user, title=Title, desc=Desc, date=Date)
    return redirect("/")


def edittaskview(request, id):
    task = ToDO.objects.get(id=id)
    try:
        print(request.method, request.POST)
        task.title = request.POST["title"]
        task.desc = request.POST["desc"]
        task.date = request.POST["date"]
        task.save()
        return HttpResponse("Success!",status=200)
    except:
        return HttpResponse("Error!",status=403)
    
