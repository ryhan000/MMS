# Generated by Django 2.1 on 2018-08-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('meal_number', models.FloatField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
