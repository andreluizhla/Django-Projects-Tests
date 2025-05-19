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

from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView, 
    View
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_completed()
        return redirect("todo_list")

