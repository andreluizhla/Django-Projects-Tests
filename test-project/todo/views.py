# Código antigo:
# from django.shortcuts import render
# from .models import Todo
# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, "todo/todo_list.html", 
#         {
#             'todos': todos
#         }
#     )

# Código Atual:
from django.views.generic import ListView

from .models import Todo

class TodoListView(ListView):
    model = Todo

