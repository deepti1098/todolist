from django.shortcuts import render, redirect
from User.models import User_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.core.mail import send_mail
from todolist import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist


def loginview(request):
    context = {"loginincorrect": False}  # check for invalid login crendentials
    if request.method == "POST":
        LEmail = request.POST["Lemail"]
        LPass = request.POST["Lpass"]
        user = authenticate(username=LEmail, password=LPass)
        if user:  # if user is valid redirect to homepage
            login(request, user)
            return redirect("/")
        else:  # else stays in login page
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
            # User is django built-in class
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
    context = {"emailincorrect": False}
    if request.method == "POST":
        email = request.POST['Lemail']

        try:  # if email exist in system
            user = User_detail.objects.get(emailid=email)

            context2 = {'email': email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'ToDoList.com',
                        # encrypted form of user primary key
                        'uid': urlsafe_base64_encode(force_bytes(user.user.pk)),
                        'user': user,
                        'token': default_token_generator.make_token(user.user),
                        'protocol': 'http', }

            emailmsg = loader.render_to_string(
                "emailtemplate.html", context2)  # rendering email template
            subject = "Reset your password"

            send_mail(subject, emailmsg,
                      settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
            return redirect("/emailsent")

        except ObjectDoesNotExist:
            context["emailincorrect"] = True
            return render(request, 'email.html', context)

    return render(request, 'email.html', context)

# To show message after submitting email for forgot password


def emailsentview(request):
    return render(request, 'email_sent.html')


def forgpassview(request, uidb64, token):
    if request.method == "POST":
        userid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=userid)
        Pass = request.POST["Lpass"]
        user.set_password(Pass)  # django function to set password
        user.save()
        logout(request)
        return render(request, 'Resetdone.html')

    return render(request, 'forgotpass.html')
