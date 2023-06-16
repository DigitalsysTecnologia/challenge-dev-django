from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.


class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    value = models.FloatField(blank=False, null=False)
    accepted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.user.name} - {self.value}'
