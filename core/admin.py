from django.contrib import admin
from .models import Course, Student, Profile, Certificate

admin.site.register([Course, Student, Profile, Certificate])
# admin.site.register(Student)
# admin.site.register(Profile)
