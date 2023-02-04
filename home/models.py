from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField()
    def __str__(self):
        return  self.Name

class Tour_Pakages(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(null=True)
    price = models.IntegerField(max_length=100)
    Days = models.IntegerField(max_length=20)
    Nights = models.IntegerField(max_length=20)
    Locations = models.CharField(max_length=300, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name