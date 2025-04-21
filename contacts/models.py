from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    pass

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    document = models.FileField(upload_to='contact_docs/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf','docx','doc','txt','ppt','pptx'])])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contacts") #we will use this to link the contact to the user

    class Meta:
        unique_together = ('user', 'email')

    def __str__(self):
        return f"{self.name} - {self.email}"

