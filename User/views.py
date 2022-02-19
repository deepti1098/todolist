import email
from django.shortcuts import render, redirect
from User.models import User_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginview(request):
    if request.method == "POST":
        LEmail = request.POST["Lemail"]
        LPass = request.POST["Lpass"]
        user = authenticate(username=LEmail, password=LPass)
        if user:
            login(request, user)

            return redirect("/")

    return render(request, 'login.html')


def signupview(request):
    context={"emailexists": False,
                "Name": "",
                "Email": "",
                "Pass": ""}
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Pass = request.POST["pass"]
        user = User.objects.get(username=Email)
        if not user:
            user = User.objects.create_user(username=Email, password=Pass)
            user_detail = User_detail.objects.create(
                user=user, name=Name, emailid=Email)

            login(request, user)
            return redirect("/")
        else:
            context["emailexists"]=True
            context["Email"]=Email
            context["Name"]=Name
            context["Pass"]=Pass
            return render(request, 'signup.html',context)

    return render(request, 'signup.html',context)


def logoutview(request):
    logout(request)
    return redirect("/")
