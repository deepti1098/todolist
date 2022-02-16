from django.db import models

class User_detail(models.Model):
    name = models.CharField(max_length=40)
    emailid = models.EmailField(primary_key=True)
    password = models.CharField(max_length=40)

