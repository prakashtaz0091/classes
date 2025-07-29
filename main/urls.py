from django.urls import path
from . import views


urlpatterns = [path("", views.home), path("tasks/create/", views.create_task)]
