from django.contrib import admin
from .models import Task, Student, School, Address, Grade, StudentProfile, Parent
# Register your models here.

admin.site.register(Task)
admin.site.register(School)
# admin.site.register(Student)
admin.site.register(Address)
admin.site.register(Grade)
admin.site.register(StudentProfile)
admin.site.register(Parent)


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile


class StudentModelAdmin(admin.ModelAdmin):
    inlines = [StudentProfileInline]

    list_display = ["name", "grade", "roll_no", "school", "address"]
    search_fields = ["name"]
    list_filter = ["grade"]


admin.site.register(Student, StudentModelAdmin)
