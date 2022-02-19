from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class User_detail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,default=1)
    name = models.CharField(max_length=40)
    emailid = models.EmailField()
    # password = models.CharField(max_length=40)

