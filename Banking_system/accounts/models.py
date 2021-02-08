from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Accounts(models.Model):
    Account_no=models.CharField(max_length=100,unique=True)
    Customer_name=models.CharField(max_length=100)
    Account_pin=models.IntegerField("Enter a pin (only digits):",unique=True)
    email=models.EmailField(max_length=200,unique=True)
    date_opened=models.DateField("date",default=datetime.date.today())
    balance_amount=models.IntegerField(default=500)


    def __str__(self):
        return self.Customer_name

class Transfer(models.Model):
    Account_no = models.CharField(max_length=100)
    to_account=models.CharField("Enter account no",max_length=100)
    amount=models.IntegerField()
    date_of_transfer=models.DateTimeField("date",default=datetime.date.today())
    def __str__(self):
        return self.Account_no








