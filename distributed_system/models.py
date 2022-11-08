from django.db import models

# Create your models here.
class Bank(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    balance=models.DecimalField(max_digits=20, decimal_places=10)
    account_number=models.IntegerField(default=0)

class Transaction(models.Model):
    sender=models.CharField(max_length=200,null=True,blank=True)
    receiver=models.CharField(max_length=200,null=True,blank=True)
    amount=models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.sender + "->" + self.receiver
    