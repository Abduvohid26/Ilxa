from django.db import models
from django.contrib.auth.models import AbstractUser

from shared.models import BaseModel
from shared.uitilty import phone_regex


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=13, unique=True, blank=False, null=False, validators=[phone_regex])
    password = models.CharField(max_length=25)
    password_confirmation = models.CharField(max_length=25)
    def __str__(self):
        return self.username

class SMSVerification(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.username} is_verified {self.is_verified}"



