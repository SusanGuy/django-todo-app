from django.shortcuts import render, get_object_or_404
from .models import Todo


def todo_list(request):
    queryset = Todo.objects.all().order_by("-published")
    context = {
        'todos': queryset
    }
    return render(request, "todo/home.html", context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})
