from django.shortcuts import render, redirect, HttpResponse
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


def deltaskview(request):
    user = User_detail.objects.get(user=request.user)
    ls = ToDO.objects.filter(user=user)
    ls.delete()

    return redirect("/")


def removetaskview(request, id):
    todo = ToDO.objects.get(id=id)
    todo.delete()
    return redirect("/")


def searchtaskview(request):

    if request.method == "POST":
        user = User_detail.objects.get(user=request.user)
        Search = request.POST["searchit"]
        ls = ToDO.objects.filter(user=user, title__contains=Search)
        context = {'todolist': ls}
        return render(request, 'list.html', context)

    return redirect("/")


def updatetaskview(request, id):
    if request.method == "POST":
        todo = ToDO.objects.get(id=id)
        todo.title = request.POST["Title"]
        todo.desc = request.POST["Desc"]
        todo.date = request.POST["Date"]
        todo.save()
        return HttpResponse("success")
    return HttpResponse("Error", status=400)
