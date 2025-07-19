from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES =[
        ('todo','ToDo'),
        ('working','Working'),
        ('done','Done')
    ]
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    comleted=models.BooleanField(default=False)
    status=models.CharField(max_length=16,choices=STATUS_CHOICES,default=False)

    def __str__(self):
        return self.description