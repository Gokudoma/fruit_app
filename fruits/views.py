from django.http import JsonResponse
from .models import Fruit
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.

@csrf_exempt
def fruit_list(request):
    if request.method == 'GET':
        fruits = Fruit.objects.all()
        data = list(fruits.values())
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        fruit = Fruit.objects.create(
            name=data['name'],
            color=data['color'],
            brand=data['brand'],
            origin=data['origin']
        )
        return JsonResponse({'status': 'Fruit created!'}, status=201)


# Daten aus der fruitsArrayBasic.txt
fruits_static_list = [
    {"name": "Apfel", "weight": 100, "color": "red", "img": "fruits/img/apfel.jpg"},
    {"name": "Banane", "weight": 120, "color": "yellow", "img": "fruits/img/banane.jpg"},
    {"name": "Orange", "weight": 150, "color": "orange", "img": "fruits/img/orange.jpg"},
    {"name": "Birne", "weight": 130, "color": "green", "img": "fruits/img/birne.jpg"},
    {"name": "Kirsche", "weight": 10, "color": "red", "img": "fruits/img/kirsche.jpg"}
]


def send_fruits(request):
    context = {
        'fruits': fruits_static_list
    }
    # Verknüpft mit fruitlist.html
    return render(request, 'fruits/fruitlist.html', context)

def info_view(request):
    # Diese View muss keine Daten übergeben, sie rendert nur das Template
    return render(request, 'fruits/info.html')