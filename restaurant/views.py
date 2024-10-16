from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    path = request.path
    response = HttpResponse('This works')
    return response


def menu(request, dish):
    menu = {
        'ugali': 'A staple food made from maize flour and water, cooked to a dense, dough-like consistency, usually served with vegetables, meat, or fish.',
        'nyama': 'Grilled or roasted meat, often goat or beef, seasoned with salt and slow-cooked over an open fire. Its typically served with kachumbari (tomato and onion salad).',
        'sukuma': 'A nutritious side dish made from collard greens sautéed with onions, tomatoes, and spices. It is often served with ugali.',
        'githeri': 'A traditional one-pot dish made from boiled maize and beans, sometimes mixed with vegetables, potatoes, or meat.',
        'chapati': 'A soft, round, flatbread made from wheat flour, water, and oil. It is often served alongside stews or curries.'
    }
    description = menu[dish]
    return HttpResponse(f"<h2> {dish}: </h2>" + description)

def book(request):
    response = HttpResponse('Make a booking')
    return response