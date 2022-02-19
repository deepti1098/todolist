from django.shortcuts import render
from .models import ToDO
from User.models import User_detail


def todoView(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    user = User_detail.objects.get(user=request.user)
    ls = ToDO.objects.filter(user=user)
    context = { 'todolist' : ls}
    return render(request, 'list.html',context)


def addtaskview(request):
    return render(request, 'additem.html')
