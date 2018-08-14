from django.db import models

# Create your models here.
class Meal(models.Model):
     name= models.CharField(max_length=200)
     meal_number=models.FloatField()
     pub_date=models.DateTimeField('date published')

     def __str__(self):
        return self.name

      