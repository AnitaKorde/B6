from unicodedata import name
from django.db import models

# Create your models here.

""" Define a custom module manager """
class activebookmanager(models.Manager):
     def get_queryset(self):
        return super(activebookmanager, self).get_queryset().filter(is_active="y")

class inactivebookmanager(models.Manager):
     def get_queryset(self):
        return super(inactivebookmanager, self).get_queryset().filter(is_active="n")

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active=models.CharField(max_length=1,default="y")

    active_obj = activebookmanager()  #its not a column feild its a functionality
    inactive_obj = inactivebookmanager() #its not a column feild its a functionality
    objects = models.Manager()

    class Meta:
        db_table="book"

    def __str__(self):
        return self.name


class Customer(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

	def __str__(self):
		return self.first_name + ' ' + self.last_name 

class Employee(models.Model):
   
    name = models.CharField(max_length=200)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
        
class Person(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
    
    class Meta:
        db_table = "person"
  
    def __str__(self):  
        return f"{self.first_name }"