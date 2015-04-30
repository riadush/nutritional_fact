from django.shortcuts import render, render_to_response, RequestContext

from models import food_nutrition


def index_view(request):
    foods = food_nutrition.objects.all()
    return render(request, 'index.html', {'foods': foods})

def single(request, nutrition_id):
    singles = food_nutrition.objects.get(pk=nutrition_id)
    return render(request, 'single.html', {'singles': singles})
