from ast import Dict, Tuple
from dataclasses import dataclass
from encodings.punycode import T
from pyexpat import model
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.http import JsonResponse

# Create your views here.

@dataclass
class SearchTerm:
    model: str
    make: str
    
    model_year: Tuple[int,int]
    
    price: Tuple[float, float]
    year: Tuple[int, int]
    stock: Tuple[int, int]
    
    additional_filters: Dict[str, Any]

#წამოიღოს ყველა
def get_all(request):
    cars = [c.to_dict() for c in Car.objects.all()]
    return JsonResponse({"cars": cars})

#წამოიღოს კონკრეტული მანქანა ID-ით
def get(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        return JsonResponse(car.to_dict())
    except Car.DoesNotExist:
        return JsonResponse({"error": "Car not found"}, status=404)


#წამოიღოს კონკრეტლი მწარმოებელის მანქანები
#api/v1/cars/make/<make:str>/
def get_by_make(request, make):
    cars = [c.to_dict() for c in Car.objects.filter(make__iexact=make)]
    return JsonResponse({"make": make, "cars": cars})

#წამოიღოს მანქანები ფასის range-ში (წამოიღოს მხოლოდ მანქანის მოდელის და მწარმოებელი)
def get_by_price_range(request, min_price, max_price):
    cars = Car.objects.filter(price__gte=min_price, price__lte=max_price)
    data = [{"make": c.make, "model": c.model} for c in cars]
    return JsonResponse({
        "min_price": float(min_price),
        "max_price": float(max_price),
        "cars": data
    })

#წამოიღოს მანქანების მოდელების სახელები (მხოლოდ სახელები ტუპლი არა) რაღაც ფასსზე ნაკლები
#ან (ფასი გაყოფილი 500) ზე stock ზე ნაკლები
def get_by_price_less_or_stock_less_then_price(request, price, stock):
    cars = Car.objects.filter(price__lt=price) | Car.objects.filter(stock__lt=stock)
    data = [c.model for c in cars] 
    return JsonResponse({"cars": data})


#ეს მერე ვქნათ
def get_by_make_or_model(request, search_term: SearchTerm):
    qs = Car.objects.all()
    
    if search_term.make:
        qs = qs.filter(make__iexact=search_term.make)
    if search_term.model:
        qs = qs.filter(model__iexact=search_term.model)
    data = [c.to_dict() for c in qs]
    return JsonResponse({"cars": data})
