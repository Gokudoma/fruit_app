from django.http import JsonResponse
from .models import Fruit
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt # Nur für dieses einfache Beispiel, um POST-Anfragen zu erlauben
def fruit_list(request):
    if request.method == 'GET':
        fruits = Fruit.objects.all()
        data = list(fruits.values())  # Konvertiert die Objekte in eine Liste von Dictionaries
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
