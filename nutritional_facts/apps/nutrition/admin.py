from django.contrib import admin

# Register your models here.

from .models import food_nutrition

class AdminFoodList(admin.ModelAdmin):
    list_display = ('User',)

admin.site.register(food_nutrition, AdminFoodList)