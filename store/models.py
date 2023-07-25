from django.db import models
from django.urls import reverse

#Importa el modelo Category del archivo models.py en la aplicación category.
from category.models import Category
# Create your models here.
# Esta es la estructura que representa al producto 
#Se define la clase Product que hereda de models.Model, lo que indica que es un modelo de base de datos.
class Product(models.Model):
# Propiedades del producto

#nombre del producto
#product_name es una propiedad de tipo CharField que representa el nombre del producto. Tiene una longitud máxima de 200 caracteres y es único.
# Unico que nos se puede repetir el nombre del producto

    product_name = models.CharField(max_length=200,unique = True)

#Slug es un concepto que se utilza en wen ecommerce que esta destinado este campo a estar dentro de la parte final del URL y representa a la entidad 

#slug es una propiedad de tipo CharField que representa el fragmento final del URL del producto. Tiene una longitud máxima de 200 caracteres y es único.


    slug = models.CharField(max_length=200,unique = True)

# slug es una propiedad de tipo CharField que representa el fragmento final del URL del producto. Tiene una longitud máxima de 200 caracteres y es único.

    description = models.TextField(max_length=500, blank = True)

#price es una propiedad de tipo IntegerField que representa el precio del producto.
    price = models.IntegerField()

#images es una propiedad de tipo ImageField que almacena las imágenes asociadas al producto. Las imágenes se cargarán en la carpeta 'photos/products'.
    images = models.ImageField(upload_to='photos/products')

#stock es una propiedad de tipo IntegerField que representa la cantidad de existencias disponibles para el producto.
    stock = models.IntegerField()

#is_avalible es una propiedad de tipo BooleanField que indica si el producto está disponible. El valor predeterminado es True.
    is_available = models.BooleanField(default=True)

#category es una propiedad de tipo ForeignKey que establece una relación con el modelo Category. Representa la categoría a la que pertenece el producto y utiliza la eliminación en cascada (on_delete=models.CASCADE) para manejar las relaciones cuando se elimina una categoría.

    category  = models.ForeignKey(Category, on_delete = models.CASCADE)

#created_date es una propiedad de tipo DateTimeField que registra la fecha y hora de creación del producto. Se establece automáticamente en el momento de la creación del objeto.

    created_date = models.DateTimeField(auto_now_add=True)

#modified_date es una propiedad de tipo DateTimeField que registra la fecha y hora de la última modificación del producto. Se actualiza automáticamente cada vez que el objeto se guarda.
    modified_date = models.DateTimeField(auto_now = True)

    def get_url(self):
      return reverse('product_detail', args=[self.category.slug,self.slug])



#El método __str__ devuelve una representación legible como cadena del objeto Product, en este caso, el nombre del producto.
    def __str__(self) -> str:
        return self.product_name
    
    #En resumen, este código define un modelo de Django para representar un producto con propiedades como nombre, descripción, precio, imágenes, disponibilidad, etc. El modelo también incluye una relación con el modelo Category para asignar cada producto a una categoría específica.