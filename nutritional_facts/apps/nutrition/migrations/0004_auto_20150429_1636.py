# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_auto_20150429_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_nutrition',
            name='Calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Calories_from_fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Cholesterol',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Date_of_entry',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 16, 36, 27, 955716)),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Fiber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Protein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Protein_unit_of_measure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Saturated_fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Sodium',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Sugars',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Total_carbohydrate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Total_fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Trans_fat',
            field=models.IntegerField(),
        ),
    ]
