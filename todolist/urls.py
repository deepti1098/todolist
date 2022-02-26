"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import search
from django.contrib import admin
from django.urls import path
from task.views import todoView, addtaskview, deltaskview, removetaskview, searchtaskview, updatetaskview
from User.views import loginview, signupview, logoutview, emailview, forgpassview,emailsentview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView, name="homepage"),
    path('login/', loginview, name="loginurl"),
    path('signup/', signupview, name="signupurl"),
    path('addtask/', addtaskview, name="additemurl"),
    path('logout/', logoutview, name="logouturl"),
    path('del/', deltaskview, name="delitemurl"),
    path('delete/<id>', removetaskview, name="getremoveurl"),
    path('search/', searchtaskview, name="searchurl"),
    path('update/<id>', updatetaskview),
    path('email/', emailview, name="emailurl"),
    path('emailsent/', emailsentview, name="emailsenturl"),
    path('forgpass/', forgpassview, name="forgpassurl")
]
