from django.db import models

# Create your models here.
class Ticket_Details(models.Model):
    IRCTC_ID = models.CharField(max_length=260,primary_key=True)
    name = models.CharField(max_length=260)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=100)
    phone=models.PositiveSmallIntegerField()
    email=models.EmailField()