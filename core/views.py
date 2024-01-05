import uuid
from random import randint
from django.utils import timezone
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

data = [
    {
        "name": "iPhone 15 Pro",
        "price": 1120,
        "quantity": 35
    },
    {
        "name": "iPhone 13 Pro",
        "price": 900,
        "quantity": 10
    },
    {
        "name": "iPhone 14 Pro",
        "price": 1090,
        "quantity": 23
    },
    {
        "name": "Samsung S23 Ultra",
        "price": 990,
        "quantity": 32
    }
]

def main_view(request: HttpRequest):
    number = randint(1, len(data))
    return render(request, "core/index.html", context={"time": timezone.now(), "number": number, "data": data})


def about_view(request: HttpRequest):
    return HttpResponse("<h1>ABOUT PAGE</h1><a href='/'>Main</a> <a href='/contact/'>Contact</a>")


def contact_view(request: HttpRequest):
    return HttpResponse("<h1>CONTACT PAGE</h1><a href='/'>Main</a> <a href='/about/'>About</a>")

def product_view(request: HttpRequest, product_token) -> HttpResponse:
    print(request.GET)
    # product = Product.objects.get(slug=slug)
    return HttpResponse(f"Products page: {request.GET.get("name")} {request.GET.get("price_min")} so'm")

def letters_view(request: HttpRequest):
    return HttpResponse(f"<h1>Letters and Digits:</h1>")



"""
'Ford': {
    'model': 'Mustang',
    'year': '1964',
},


"""