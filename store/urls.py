
# django.urls: la función path y el módulo views del directorio actual (.).
from django.urls import path
from . import views

#La ruta path('', views.store, name='store') se define utilizando la función path. Esta ruta tiene tres argumentos:

#El primer argumento '' es una cadena vacía, lo cual indica que esta ruta coincide con la URL raíz de tu sitio web. Es decir, cuando se accede a la URL base del sitio, esta ruta se activará.

#El segundo argumento views.store se refiere a una función store que se encuentra en el módulo views que has importado previamente. Esta función manejará la lógica para responder a la solicitud de esta ruta en particular.

#El tercer argumento name='store' es un nombre opcional que se puede usar para referirse a esta ruta en otras partes del código. En este caso, se le ha dado el nombre 'store'

urlpatterns = [
    path('',views.store,name="store"),
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
]


