from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    fullName = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phoneNumber = models.IntegerField(default=254728403916, null=True, blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.fullName
    

class Employee(models.Model):
    
    AVAILABILITY_STATUS = [
        ("Not available", "Not available"),
        ("Available", "Available"),
        ("Immediate", "Immediate"),
    ]

    name = models.CharField(max_length=200, null=True)
    speciality = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default=0, null=True)
    salary_expectation = models.FloatField()
    availability = models.BooleanField(max_length=100, choices=AVAILABILITY_STATUS,null=True, blank=True)
    slug = models.SlugField(unique=True)
    joined_on = models.DateTimeField(auto_now_add=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['joined_on']


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_booked = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return  self.date_booked
    
    class Meta:
        ordering = ['date_booked']

class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    sku = models.SlugField(max_length=200, null=True, blank=True)
    service_id = models.IntegerField(null=True)