from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/create/", views.create_task),
    # path("schools/", views.schools),
    path("schools/", views.SchoolView.as_view(), name="schools_list"),
    path("schools/<pk>/view/", views.SchoolDetail.as_view(), name="school_detail"),
    path("schools/create/", views.SchoolCreate.as_view(), name="create_school"),
    path("schools/<pk>/", views.SchoolUpdate.as_view(), name="update_school"),
    path("schools/<pk>/delete/", views.SchoolDelete.as_view(), name="delete_school"),
]
