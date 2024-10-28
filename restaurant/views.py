from django.shortcuts import render
from django.http import HttpResponse
from restaurant.forms import ApplicationForm, CustomerForm
from .models import Menu


def home(request):
    path = request.path
    response = HttpResponse('This works')
    return response


def about(request):
    about_content = {'about': 'We are based in Kericho as the best hotel hagdhjjhjhjhjhjjhjhjhjhasdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'}
    return render(request, 'about.html', {'content':about_content})


def menu(request, dish):
    menu = {
        'ugali': 'A staple food made from maize flour and water, cooked to a dense, dough-like consistency, usually served with vegetables, meat, or fish.',
        'nyama': 'Grilled or roasted meat, often goat or beef, seasoned with salt and slow-cooked over an open fire. Its typically served with kachumbari (tomato and onion salad).',
        'sukuma': 'A nutritious side dish made from collard greens sautéed with onions, tomatoes, and spices. It is often served with ugali.',
        'githeri': 'A traditional one-pot dish made from boiled maize and beans, sometimes mixed with vegetables, potatoes, or meat.',
        'chapati': 'A soft, round, flatbread made from wheat flour, water, and oil. It is often served alongside stews or curries.'
    }
    
    # description = menu[dish]
    # return HttpResponse(f"<h2> {dish}: </h2>" + description)
    return render (request, 'menu.html',{'context':menu})

def menu_by_id(request):
  newmenu = Menu.objects.all()
  newmenu_dict = {'menu': newmenu}
  return render(request, 'menu_card.html',newmenu_dict)


def book(request):
    response = HttpResponse('Make a booking')
    return response

def form_view(request):
    form = ApplicationForm
    context = {"form":form}
    return render(request, "apply.html",context)

def customer_view(request):
    form = CustomerForm
    if request.method =='POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "apply.html",context)