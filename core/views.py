from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


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
    print("Someone made request in courses page")

def about(request):
    print("Someone made request in about page")
    return HttpResponse("this is about page.")
