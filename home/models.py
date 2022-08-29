from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError




# Create your models here.
class Contact(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=233, blank=True)
    desc = models.CharField(max_length=233, blank=True)
    user_id = models.IntegerField(blank=True, default=1)
    accepted = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.name)
    