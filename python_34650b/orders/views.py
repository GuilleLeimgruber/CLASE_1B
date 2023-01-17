from django.shortcuts import render

from orders.models import Orders


from django.http import HttpResponse
# Create your views here.




def list_orders(request):
    orders = Orders.objects.all()
    context = {
        'orders': orders,
    }
    
    return render(request, 'Orders/list_orders.html', context=context)

def create_order(request):
        Orders.objects.create(client='Guillermo Leimgruber', product= 'Curso de Python', payment_method= 'Card')
        return HttpResponse('Orden creada')