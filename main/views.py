from django.shortcuts import render, redirect
from .models import Task


def home(request):
    # print("This is home page")

    tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "main/home.html", context)


def create_task(request):
    if request.method == "POST":
        print("-------------This is post request-------------------")
        data = request.POST
        task_title = data.get("title")
        task_desc = data.get("desc")

        Task.objects.create(title=task_title, desc=task_desc)

        return redirect(home)

    return render(request, "main/create-task.html")
