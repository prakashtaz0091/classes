from django.contrib import admin
from django.urls import path
from core.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("contact/", contact),
    path("about/", about),
    path("courses/<course_id>/", course_detail, name="course_detail"),
    path("courses/", courses, name="courses"),
]
