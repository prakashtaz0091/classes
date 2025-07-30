from django.shortcuts import render, redirect
from .models import Task, School
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy


class SchoolDelete(DeleteView):
    model = School
    success_url = reverse_lazy("schools_list")


class SchoolUpdate(UpdateView):
    model = School
    fields = "__all__"
    success_url = reverse_lazy("schools_list")


class SchoolCreate(CreateView):
    model = School
    fields = "__all__"
    success_url = reverse_lazy("schools_list")


class SchoolDetail(DetailView):
    model = School


class SchoolView(ListView):
    model = School


# def school_detail(request, school_id):
#     print("School detail page", school_id)
#     return Http404("School not found")


# def schools(request):
#     print("Schools page")


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
