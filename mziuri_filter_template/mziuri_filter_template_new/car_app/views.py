from ast import Dict, Tuple
from dataclasses import dataclass
from encodings.punycode import T
from pyexpat import model
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
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
    data = Car.objects.all()
    pass
#წამოიღოს კონკრეტული მანქანა ID-ით
def get(request, car_id):
    pass

#წამოიღოს კონკრეტლი მწარმოებელის მანქანები
#api/v1/cars/make/<make:str>/
def get_by_make(request, make):
    pass

#წამოიღოს მანქანები ფასის range-ში (წამოიღოს მხოლოდ მანქანის მოდელის და მწარმოებელი)
def get_by_price_range(request, min_price, max_price):
    pass

#წამოიღოს მანქანების მოდელების სახელები (მხოლოდ სახელები ტუპლი არა) რაღაც ფასსზე ნაკლები
#ან (ფასი გაყოფილი 500) ზე stock ზე ნაკლები
def get_by_price_less_or_stock_less_then_price(request, price, stock):
    pass

#ეს მერე ვქნათ
def get_by_make_or_model(request, search_term:SearchTerm):
    pass