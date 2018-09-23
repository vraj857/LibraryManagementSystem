
from django.contrib.auth.models import AbstractUser
from django.db import models

#Create your models here.
class UserRole(models.Model):
    user_role_id = models.PositiveSmallIntegerField(primary_key=True)
    user_role_name = models.CharField(max_length=32)
    user_role_description = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return self.user_role_name


class User(AbstractUser):
    user_role = models.ForeignKey(UserRole,to_field='user_role_id', default=2)
    #user_role = models.ForeignKey(UserRole)
    login_attempts = models.PositiveSmallIntegerField(default=0)
    account_locked_dt = models.DateTimeField(null=True,blank=True)



    def get_login_attempts(self):
        return self.login_attempts














