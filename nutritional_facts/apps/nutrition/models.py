from django.db import models
import datetime

# Create your models here.

class food_nutrition(models.Model):
    User = models.CharField(max_length=120, unique=True)
    Date_of_entry = models.DateTimeField(default=datetime.datetime.now())
    Name_of_food = models.CharField(max_length=250)
    Number_of_servings = models.IntegerField()
    Serving_size_amount = models.IntegerField()
    Serving_size_unit_of_measure = models.CharField(max_length=120)
    Calories = models.IntegerField()
    Calories_from_fat = models.IntegerField()
    Total_fat = models.IntegerField()
    Trans_fat = models.IntegerField()
    Saturated_fat = models.IntegerField()
    Cholesterol = models.IntegerField()
    Cholesterol_unit_of_measure = models.CharField(max_length=250)
    Sodium = models.IntegerField()
    Sodium_unit_of_measure = models.CharField(max_length=250)
    Total_carbohydrate = models.IntegerField()
    Total_carbohydrate_unit_of_measure = models.CharField(max_length=250)
    Fiber = models.IntegerField()
    Fiber_unit_of_measure = models.CharField(max_length=250)
    Sugars = models.IntegerField()
    Sugars_unit_of_measure = models.CharField(max_length=250)
    Protein = models.IntegerField()
    Protein_unit_of_measure = models.IntegerField()
    Vitamin_A = models.IntegerField(blank=True)
    Vitamin_C = models.IntegerField(blank=True)
    Calcium = models.IntegerField(blank=True)
    Iron = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.User