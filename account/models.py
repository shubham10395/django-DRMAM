from django.db import models
from django.contrib.auth.models import User


class labinfo(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    lab_incharge = models.CharField(max_length=50)
    no_of_pc = models.IntegerField()
    ram = models.IntegerField()
    starage = models.IntegerField()
    name_of_os = models.CharField(max_length=50)
    #user_id = models.IntegerField()
    account_labinfo_id =  models.IntegerField()

class classinfo(models.Model):
    #student = models.ForeignKey(student,on_delete=models.CASCADE)
    strength = models.IntegerField(default=1)
    projector = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    #user_id = models.IntegerField()
    account_classinfo_id =  models.IntegerField()
