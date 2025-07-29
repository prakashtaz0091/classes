from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.title


# class CustomUser(models.Model):
#     username =


class School(models.Model):
    name = models.CharField(max_length=300)
    estd_date = models.DateField()

    def __str__(self):
        return self.name


class Address(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Addresses"


class Grade(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    room_no = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.school} | {self.name}"


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=150)
    roll_no = models.IntegerField()
    address = models.ForeignKey(
        Address, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to="student_photos", null=True, blank=True)

    def __str__(self):
        return f"{self.student}'s profile"


class Parent(models.Model):
    name = models.CharField(max_length=200)

    children = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
