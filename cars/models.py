from django.db import models

from cars.utils import expense_transaction_id, revenue_transaction_id

# Create your models here.
class Car(models.Model):
    matricule = models.CharField(max_length=10,unique=True)
    car_type = models.CharField(max_length=40)
    date_bought = models.DateField()
    date_put_to_use = models.DateField()
    price = models.IntegerField()
    kilometres_bought_with = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_created=True,auto_now_add=True)

    def __str__(self):
        return self.matricule

class CarDocument(models.Model):
    type = models.CharField(max_length=256)
    amount = models.DecimalField(decimal_places=0, max_digits=20)
    description = models.TextField(blank=True)
    date_paid = models.DateField()
    expiry_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='documents/images/')

class Expense(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    amount = models.DecimalField(decimal_places=0, max_digits=20)
    description = models.TextField()
    date = models.DateTimeField(auto_created=True,auto_now_add=True)
    transaction_id = models.CharField(max_length=256,editable=False,unique=True,default=expense_transaction_id)

    def __str__(self):
        return self.name

    def total_amount(self):
        transaction = self.all()
        total = 0
        for t in transaction:
            total += t.amount
        
        return total

class Revenue(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    amount = models.DecimalField(decimal_places=0, max_digits=20)
    description = models.TextField()
    date = models.DateTimeField(auto_created=True,auto_now_add=True)
    transaction_id = models.CharField(max_length=256,editable=False,unique=True,default=revenue_transaction_id)

    def __str__(self):
        return self.name

