from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # ID field, automatically incrementing
    name = models.CharField(max_length=255)  # Name field, varchar type in MySQL
    no_of_guests = models.IntegerField()     # Number of guests, integer type
    booking_date = models.DateField()        # Booking date, date type

    def __str__(self):
        return f"{self.name} - {self.booking_date}"

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # ID field, automatically incrementing
    title = models.CharField(max_length=255) # Title of the menu item
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price field with 2 decimal places
    inventory = models.IntegerField()        # Inventory field, integer type

    def __str__(self):
        return f"{self.title} - ${self.price}"
