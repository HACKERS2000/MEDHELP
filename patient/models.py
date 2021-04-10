from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
