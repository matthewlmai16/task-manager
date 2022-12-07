from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(False)
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }

    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_task(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {"my_task": tasks}
    return render(request, "tasks/my_task.html", context)
