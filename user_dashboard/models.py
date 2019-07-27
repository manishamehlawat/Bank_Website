from django.db import models

# Create your models here.
class account_details(models.Model):
    Account_number=models.CharField(max_length=14)
    Email=models.EmailField(max_length=40)
    Phone_no=models.BigIntegerField()

class deposit(models.Model):
       Account_number=models.CharField(max_length=14)
       Date=models.DateTimeField()
       Amount=models.IntegerField()
       
class withdraw(models.Model):
     Account_number=models.CharField(max_length=14)
     Date=models.DateTimeField()
     Amount=models.IntegerField()
     
class total_money(models.Model):
    Account_number=models.CharField(max_length=14)
    Balance=models.IntegerField()
    
    
    
    
