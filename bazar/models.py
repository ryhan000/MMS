from django.db import models


class Bazar(models.Model):
    name = models.CharField(max_length=200)
    amount=models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Item(models.Model):
    bazar = models.ForeignKey(Bazar, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200,blank=True, null=True)
    amount=models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.item_name

