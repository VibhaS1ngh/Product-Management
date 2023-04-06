from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=128,null=True,blank=True)
    mobile=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=254,unique=True, null=True, blank=True)
    password=models.CharField(max_length=128,null=True,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name','mobile']

    class Meta:
        db_table='user'
        verbose_name= "User"

    def __str__(self):
        return "{}".format(self.email)

class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=128,blank=True,null=True)
    category=models.CharField(max_length=128,blank=True,null=True)
    brand=models.CharField(max_length=128,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=False)
    description=models.TextField(max_length=1000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='product'
        verbose_name="Product"
    def __str__(self):
        return "{}".format(self.name)
