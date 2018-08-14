from django.db import models

class Registration(models.Model):
	
     name= models.CharField(max_length=200)
     phn=models.CharField(max_length=20)
     regi_date=models.DateTimeField('date published')

     def __str__(self):
        return self.name