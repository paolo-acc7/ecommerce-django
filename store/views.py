from django.shortcuts import render ,get_object_or_404
# importar la clase Product del models.py 
from .models import Product
from category.models import Category

# Create your views here.

# El código que has proporcionado importa la función render del módulo django.shortcuts. La función render se utiliza para renderizar una plantilla y devolver una respuesta HTTP al cliente.

#La línea def store(request): define una función llamada store que toma un argumento request. En Django, una función de vista toma una solicitud (request) como argumento y devuelve una respuesta.

#Dentro de la función store, se llama a render para renderizar una plantilla llamada 'store/store.html'. La función render toma dos argumentos: la solicitud (request) y el nombre de la plantilla a renderizar.

#En resumen, este código define una función de vista llamada store que toma una solicitud como argumento. Dentro de la función, se utiliza la función render para renderizar la plantilla 'store/store.html' y devolver la respuesta correspondiente.


def store(request, category_slug=None):
    #Dentro de la vista, se realiza una consulta a la base de datos utilizando el modelo Product. Se obtienen todos los objetos Product mediante el método all(), y se filtran solo aquellos productos que tienen el atributo is_available establecido como True. Los resultados se almacenan en la variable products.

#A continuación, se cuenta la cantidad de productos obtenidos utilizando el método count() y se almacena en la variable products_count.

    categories = None
    products = None
    
    if category_slug  != None :
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else : 
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()



#Luego, se crea un diccionario context que contiene las variables products y products_count. Este diccionario se utiliza para pasar los datos a la plantilla HTML.
    context = {
        
               'products':products, 
               'products_count':product_count,
    }
    
#Por último, se llama a la función render pasando el objeto request, la ruta de la plantilla store/store.html y el diccionario context. Esto renderiza la plantilla HTML con los datos proporcionados y devuelve una respuesta HTTP que puede ser enviada al navegador del cliente.
    return render(request, 'store/store.html',context)

def  product_detail(request, category_slug, product_slug):
#
    try:
         single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context ={
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html' , context)


