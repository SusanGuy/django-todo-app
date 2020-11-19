from django.shortcuts import render
from .models import Todo


def todo_list(request):
    queryset = Todo.objects.all().order_by("-published")
    context = {
        'todos': queryset
    }
    return render(request, "todo/home.html", context)
