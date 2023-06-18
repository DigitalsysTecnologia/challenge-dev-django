import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.


class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.name}'


class Proposal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.FloatField(blank=False, null=False)
    accepted = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'{self.user.name} - {self.value}'
