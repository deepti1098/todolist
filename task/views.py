from django.shortcuts import render


def todoView(request):
    return render(request, 'list.html')


def addtaskview(request):
    return render(request, 'additem.html')
