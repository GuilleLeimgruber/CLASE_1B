from django.urls import path

from orders.views import list_orders, create_order




urlpatterns = [
    path('lista_de_ordenes/', list_orders),
    path('Creacion_de_ordenes/', create_order),
    
]