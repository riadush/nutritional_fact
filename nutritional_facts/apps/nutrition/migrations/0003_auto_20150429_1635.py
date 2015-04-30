# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_auto_20150429_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_nutrition',
            name='Date_of_entry',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 16, 35, 26, 860646)),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Number_of_servings',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Serving_size_amount',
            field=models.IntegerField(blank=True),
        ),
    ]
