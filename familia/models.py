from turtle import clear
from django.db import models
from unittest.util import _MAX_LENGTH
from mailbox import NoSuchMailboxError


class Familiar(models.Model):
    nombre = models.CharField(max_length=30 )
    apellido = models.CharField(max_length=30 )
    edad = models.IntegerField(null=True)
    fecha = models.DateField(null=True)