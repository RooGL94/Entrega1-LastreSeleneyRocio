from django.shortcuts import render
from products.models import cositas 

# Create your views here.


from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from products.forms import product_form
from products.models import cositas, ofertas, segunda_mano
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from products.forms import User_registration_form
from django.contrib.auth.decorators import login_required


def logout_view(request):
    logout(request)
    return redirect('inicio')


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message':f'bienvenido, {username}'}
                return render(request, 'inicio.html', context=context)
            else:
                context= {'errors': 'No existe el usuario'}
                form=AuthenticationForm()
                return render(request, 'auth/login.html', context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors': errors, 'form': form}
            return render(request, 'auth/login.html', context = context)

            
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context=context)



def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido! {username}'}
            return render(request, 'inicio.html', context =context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context =context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)




def inicio(request):
    return render(request, 'inicio.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

@login_required
def create_product(request):
    if request.method == 'GET':
        form = product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            new_product = cositas.objects.create(
                Nombre= form.cleaned_data['nombre'],
                Precio= form.cleaned_data['precio'],
                Detalles= form.cleaned_data['detalles'],
                Imagen= form.cleaned_data ['imagen']
            )
            context = {'new_product':new_product}
        return render(request, 'create_product.html', context=context)



def productos_all(request):
    productos_all= cositas.objects.all()
    context= {"productos_all":productos_all}
    return render(request, "Productos.html", context=context)        



def search_product_views(request):
    products = cositas.objects.filter(Nombre__icontains=request.GET['search'])
    context = {'products':products}
    return render(request, 'search_product.html', context)

def ofertas_all(request):
    ofertas_all= ofertas.objects.all()
    context={"ofertas_all":ofertas_all}
    return render(request, "ofertas.html", context=context)
    

def segunda_mano_all(request):
    segunda_mano_all= segunda_mano.objects.all()
    context= {"segunda_mano_all":segunda_mano_all}
    return render(request, "segunda_mano.html", context=context)        


