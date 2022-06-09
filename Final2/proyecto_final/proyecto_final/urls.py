"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import productos_all, search_product_views
from products.views import inicio
from products.views import sobre_nosotros
from products. views import create_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', productos_all, name = 'productos'),
    path('inicio/', inicio, name= 'inicio'),
    path('aboutus/', sobre_nosotros, name= 'aboutus'),
    path('create-product/', create_product, name= 'create-product'),
    path('search-product/', search_product_views, name= 'search_product_views')
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

