from django.db import models

# Create your models here.
class tweeter(models.Model):
    person=models.CharField(max_length=50)
    dop=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    caption=models.CharField(max_length=150)


    def __str__(self):
        return self.person

class Manufacturer(models.Model):
    brand=models.CharField(max_length=50)
    ceo=models.CharField(max_length=50)
    turnover=models.IntegerField()
    def __str__(self):
        return self.brand

class Car(models.Model):
    name=models.CharField(max_length=70)
    year=models.IntegerField()
    mileage=models.IntegerField()
    fuel=models.CharField(max_length=50)
    manufacture=models.Foreignkey("Manufacturer",on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class tweeter1(models.Model):
    person=models.CharField(max_length=50)
    dop=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=150)


    def __str__(self):
        return self.person
