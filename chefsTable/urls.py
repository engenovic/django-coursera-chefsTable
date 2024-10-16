from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls'))
]

handler404 = 'chefsTable.views.handler404'