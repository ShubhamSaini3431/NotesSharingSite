from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    contact = models.CharField(max_length=10)
    branch = models.CharField(max_length=30)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uploading_date = models.CharField(max_length=10, null=True)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    notesfile = models.FileField()
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.subject
