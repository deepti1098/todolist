from django.shortcuts import render, redirect
from User.models import User_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
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
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Pass = request.POST["pass"]

        user = User.objects.create_user(username=Email, password=Pass)
        user_detail = User_detail.objects.create(
            user=user, name=Name, emailid=Email)

        login(request, user)

        return redirect("/")

    return render(request, 'signup.html')


def logoutview(request):
    logout(request)
    return redirect("/")
