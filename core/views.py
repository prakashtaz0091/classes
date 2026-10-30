from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


def course_detail(request, course_id):
    # print("User clicked ", course_id)
    course = Course.objects.get(id=course_id)
    # print(course)

    return render(request, "core/course_detail.html", {
        'course':course
    })

def home(request):
    print("Someone made request in home page")
    
    courses = Course.objects.all()
    user_authenticated = False
    
    # for course in courses:
    #     course["offer_price"] = course["price"]-(course["price"] * course["discount_percentage"]) / 100   
    # print(courses)
    return render(request, "core/home.html", {
        "courses": courses,
        "user_authenticated": user_authenticated
    })

def contact(request):
    print("Someone made request in contact page")

def courses(request):
    search = request.GET.get("search")
    # print("User is searching for ", request.GET.get("search"))
    courses = Course.objects.filter(name__icontains=search)
    
    return render(request, "core/courses.html", {
        'courses':courses
    })

def about(request):
    print("Someone made request in about page")
    return HttpResponse("this is about page.")
