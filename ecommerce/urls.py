"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.contrib import admin: Importamos el módulo admin de Django, el cual nos permite crear un panel de administración para nuestra aplicación.
from django.contrib import admin
#from django.urls import path: Importamos el módulo path de Django, el cual nos permite definir las URL's de nuestra aplicación.
from django.urls import path , include
#from . import views: Importamos el archivo views.py de nuestra aplicación.
from . import views
# importamos la siguiente modulo o libreria 
#from django.conf.urls.static import static: Importamos la función static del módulo django.conf.urls.static, la cual nos permite servir archivos estáticos como imágenes, archivos CSS, archivos JavaScript, etc.
from django.conf.urls.static import static
#imporamos el siguiente modulo o libreria
#from django.conf import settings: Importamos el módulo settings de Django, el cual nos permite acceder a las configuraciones de nuestra aplicación.
from django.conf import settings



urlpatterns = [
    # path('admin/', admin.site.urls),: Agregamos la URL /admin/ a nuestra lista de URL's, la cual apunta al panel de administración de Djang
    path('admin/', admin.site.urls),
    
    #path('',views.home, name= "home"),: Agregamos la URL principal de nuestra aplicación, la cual apunta a la vista home definida en el archivo views.py y le asignamos un nombre llamado home.
    path('',views.home, name= "home"),

#   Quiero que me redireccione a la app store y a futuro voy a crear otro archivo de tipo URL que procese este pedido y me redirrecione a la app principal store 

    path('store/', include('store.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT): Agregamos la configuración necesaria para servir archivos estáticos, utilizando la función static y pasando las configuraciones MEDIA_URL y MEDIA_ROOT definidas en el archivo settings.py de nuestra aplicación.
