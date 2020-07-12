from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    height = models.IntegerField()
    sex = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.user
