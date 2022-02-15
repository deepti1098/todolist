from django.shortcuts import render
from .models import todolistItems

def todoView(request):
    all_todo_items = todolistItems.objects.all()
    return render(request, 'todolist.html', {'all_items' : all_todo_items})
    
