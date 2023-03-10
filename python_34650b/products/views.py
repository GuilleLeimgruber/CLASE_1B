from django.shortcuts import render

from django.http import HttpResponse

from products.models import Products, Category


# Create your views here.
def create_product(request):

    
    new_product= Products.objects.create(name = 'Cerveza Imperial Apa 1L', price = 450, stock = True)
   
    print(new_product)
    return HttpResponse('Se creo el nuevo producto')


def list_products(request):
    all_products = Products.objects.all
    print(all_products)
    context = {'products': all_products}


    return render(request, 'Products/list_products.html', context = context)


def saludo(request):
    return HttpResponse("Hola")

def list_categories(request):
    all_categories = Category.objects.all
    
    context = {'categories': all_categories}
    return render(request, 'Categories/list_categories.html', context = context)


def create_category(request, name):

    
    Category.objects.create(name = name)
    
    return HttpResponse('Se creo una nueva categoria')

