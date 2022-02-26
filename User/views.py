from django.shortcuts import render, redirect
from User.models import User_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.mail import send_mail
from todolist import settings
# Create your views here.


def loginview(request):
    context = {"loginincorrect": False}
    if request.method == "POST":
        LEmail = request.POST["Lemail"]
        LPass = request.POST["Lpass"]
        user = authenticate(username=LEmail, password=LPass)
        if user:
            login(request, user)
            return redirect("/")
        else:
            context["loginincorrect"] = True
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def signupview(request):
    context = {"emailexists": False,
               "Name": "",
               "Email": "",
               "Pass": ""}
    if request.method == "POST":
        Name = request.POST["name"]
        Email = request.POST["email"]
        Pass = request.POST["pass"]

        try:
            user = User.objects.create_user(username=Email, password=Pass)
            user_detail = User_detail.objects.create(
                user=user, name=Name, emailid=Email)

            login(request, user)
            return redirect("/")
        except IntegrityError:
            context["emailexists"] = True
            context["Email"] = Email
            context["Name"] = Name
            context["Pass"] = Pass
            return render(request, 'signup.html', context)

    return render(request, 'signup.html', context)


def logoutview(request):
    logout(request)
    return redirect("/")


def emailview(request):
    return render(request, 'email.html')

def emailsentview(request):
    if request.method == "POST":
        email = request.POST['Lemail']
        send_mail('Password Reset','You can reset you password',settings.DEFAULT_FROM_EMAIL,[email],fail_silently=False)
    return render(request, 'email_sent.html')

def forgpassview(request):
    
    return render(request, 'forgotpass.html')
