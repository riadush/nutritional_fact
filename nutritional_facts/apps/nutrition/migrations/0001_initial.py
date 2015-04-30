# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food_nutrition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User', models.CharField(unique=True, max_length=120)),
                ('Date_of_entry', models.DateTimeField(default=datetime.datetime(2015, 4, 28, 16, 58, 36, 892096))),
                ('Name_of_food', models.CharField(max_length=250)),
                ('Number_of_servings', models.IntegerField(blank=True)),
                ('Serving_size_amount', models.IntegerField(blank=True)),
                ('Serving_size_unit_of_measure', models.CharField(max_length=120)),
                ('Calories', models.IntegerField(blank=True)),
                ('Calories_from_fat', models.IntegerField(blank=True)),
                ('Total_fat', models.IntegerField(blank=True)),
                ('Trans_fat', models.IntegerField(blank=True)),
                ('Saturated_fat', models.IntegerField(blank=True)),
                ('Cholesterol', models.IntegerField(blank=True)),
                ('Cholesterol_unit_of_measure', models.CharField(max_length=250)),
                ('Sodium', models.IntegerField(blank=True)),
                ('Sodium_unit_of_measure', models.CharField(max_length=250)),
                ('Total_carbohydrate', models.IntegerField(blank=True)),
                ('Total_carbohydrate_unit_of_measure', models.CharField(max_length=250)),
                ('Fiber', models.IntegerField(blank=True)),
                ('Fiber_unit_of_measure', models.CharField(max_length=250)),
                ('Sugars', models.IntegerField(blank=True)),
                ('Sugars_unit_of_measure', models.CharField(max_length=250)),
                ('Protein', models.IntegerField(blank=True)),
                ('Protein_unit_of_measure', models.IntegerField(blank=True)),
                ('Vitamin_A', models.IntegerField(blank=True)),
                ('Vitamin_C', models.IntegerField(blank=True)),
                ('Calcium', models.IntegerField(blank=True)),
                ('Iron', models.IntegerField(blank=True)),
            ],
        ),
    ]
