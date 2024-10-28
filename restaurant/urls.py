from django.urls import path 
from .import views

urlpatterns = [
    path('home/',views.home),
    path('about/',views.about),
    path('menu/',views.menu),
    #path('menu/<str:dish>',views.menu),
    path('menu_card/',views.menu_by_id),
    path('apply/',views.form_view),
    path('reserve/',views.customer_view),
]
