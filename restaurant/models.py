from django.db import models


class MenuCategory(models.Model): 
    menu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_name
class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    cuisine = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default= None,related_name="category_name" )
 
    def __str__(self):
       return f"{self.name} {self.price}"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
