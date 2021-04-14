from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=255, null=True)
    email=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url= models.CharField(max_length=2083, null=True)
    image= models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd= models.DateTimeField(auto_now_add=True)
    complete= models.BooleanField(default=False, null=True, blank=False)
    transaction_id= models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)










class Offer(models.Model):
    code = models.CharField(max_length=10)
    description= models.CharField(max_length=256)
    discount = models.FloatField()