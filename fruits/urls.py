from django.urls import path
from . import views

urlpatterns = [
    path('fruits/', views.fruit_list),
    path('list/', views.send_fruits),
]