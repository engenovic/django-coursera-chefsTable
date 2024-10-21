from django.urls import path 
from .import views

urlpatterns = [
    path('home/',views.home),
    path('menu/<str:dish>',views.menu),
    path('apply/',views.form_view),
    path('reserve/',views.customer_view),
]
