from django.db import models
from User.models import User_detail
import datetime


class ToDO(models.Model):
    user = models.ForeignKey(
        User_detail, on_delete=models.CASCADE, null=False, default=1)
    title = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(blank=True, default=datetime.datetime.now())
