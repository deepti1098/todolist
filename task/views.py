from django.shortcuts import render, redirect
from .models import ToDO
from User.models import User_detail


def todoView(request):
    if not request.user.is_authenticated:
        return redirect("login/")
    user = User_detail.objects.get(user=request.user)
    ls = ToDO.objects.filter(user=user)
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
