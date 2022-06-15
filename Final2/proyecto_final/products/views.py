from django.shortcuts import render
from products.models import cositas 

# Create your views here.


from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from products.forms import product_form
from products.models import cositas 



def inicio(request):
    return render(request, 'inicio.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def create_product(request):
    if request.method == 'GET':
        form = product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            new_product = cositas.objects.create(
                Nombre= form.cleaned_data['Nombre'],
                Precio= form.cleaned_data['Precio'],
                Detalles= form.cleaned_data['Detalles'],
                Imagen= form.cleaned_data ['Imagen']
            )
            context = {'new_product':new_product}
        return render(request, 'create_product.html', context=context)  



def productos_all(request):
    productos_all= cositas.objects.all()
    context= {"productos_all":productos_all}
    return render(request, "Productos.html", context=context)        



def search_product_views(request):
     #product = products.objects.GET()
    products = cositas.objects.filter(Nombre__icontains=request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context)