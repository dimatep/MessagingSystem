from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# here is my data base - define classes or new types


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.CharField(max_length=300, default='Enter your message (max 300 chars)')
    subject = models.CharField(max_length=50, default='Enter your subject (max 50 chars)')
    creation_date = models.DateField()

    def __str__(self):
        return self.message


