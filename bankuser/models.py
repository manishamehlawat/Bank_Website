from django.db import models

# Create your models here.
class banking(models.Model):
    
    Name=models.CharField(max_length=40)
    Phone_no=models.BigIntegerField()
    Email=models.EmailField(max_length=40)
    Password=models.CharField(max_length=40)
    Count=models.IntegerField()
    Date=models.DateTimeField()
   