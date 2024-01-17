from django.shortcuts import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    isActive=True
    if request.method=="POST":
        check=request.POST.get("check")
        print(check)
        if check is None: isActive=False
        else: isActive=True



    date=datetime.datetime.now()
   
    name="Mohammed Farhan Mohiuddin"
    list_of_programs=[
        "W.A.P to check even or odd"
        "W.A.P to prime number"
        "W.A.P to print all prime from 1 to 100"
        "W.A.P to print pascals triangle"
    ]
    student={
        'student_name':"Farhan",
        'student_college':"MJ",
        "student_city":"Hyderabad"
    }

    data={
        'name':name,
        'date':date,
        'isActive':isActive,
        'list_of_programs':list_of_programs,
        'student_data':student
    }

    return render(request,"home.html",data)

def about(request):
    return render (request, "about.html",{})

def services(request):
    return render (request, "services.html",{})
