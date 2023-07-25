#•	La primera línea importa la función render desde el módulo shortcuts en el paquete django, que se utiliza para renderizar plantillas en una respuesta HTTP.
from django.shortcuts import render
# •	La segunda línea importa el modelo Product desde el módulo models del paquete store. Esto supone que tienes un modelo llamado Product definido en un archivo models.py dentro de la aplicación store.
from store.models import Product
#•	La función home es una vista que se utiliza para manejar una solicitud HTTP entrante. Toma un argumento request que representa la solicitud HTTP recibida.
def home(request):

     #•	La siguiente línea obtiene todos los objetos Product del modelo Product mediante la llamada a Product.objects.all(). Luego se aplica un filtro .filter(is_available=True) para obtener solo los productos que están disponibles.
     products = Product.objects.all().filter(is_available=True)
# •	Después, se crea un diccionario context que contiene una clave llamada products con el valor de la variable products obtenida anteriormente.
     context = {'products': products, 
                
     }
     
     # •	Finalmente, se llama a la función render para renderizar la plantilla 'home.html' utilizando el contexto context y se devuelve el resultado como respuesta a la solicitud HTTP.
     return render(request, 'home.html' , context)