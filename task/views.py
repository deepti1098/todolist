from django.shortcuts import render


def todoView(request):
    return render(request, 'todolist.html')
    
