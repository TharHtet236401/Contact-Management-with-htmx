from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contacts") #we will use this to link the contact to the user

    class Meta:
        unique_together = ('user', 'email')

    def __str__(self):
        return f"{self.name} - {self.email}"

