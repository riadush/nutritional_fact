# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_auto_20150429_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_nutrition',
            name='Date_of_entry',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 29, 16, 36, 47, 538765)),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Number_of_servings',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='food_nutrition',
            name='Serving_size_amount',
            field=models.IntegerField(),
        ),
    ]
