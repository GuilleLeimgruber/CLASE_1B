from django.urls import path

from products.views import create_product, list_products, saludo, list_categories, create_category




urlpatterns = [
    path('Creacion_producto/', create_product),
    path('lista_de_productos/', list_products),
    path('saludito/', saludo),
    path('lista_de_categorias/', list_categories),
    path('Creacion_categoria/<str:name>/', create_category),
]