from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    created_by=models.CharField(max_length=50,default=None,null=True)
    modified=models.DateTimeField(auto_now=True)
    STATUS = (
       ('ticket open','ticket open'),
       ('ticket under review','ticket under review'),
       ('ticket closed','closed'),
   )
    status=models.CharField(max_length=45,choices=STATUS,default='open')
    ticket_name=models.CharField(max_length=50)
    ticket_description=models.TextField(max_length=200)
    