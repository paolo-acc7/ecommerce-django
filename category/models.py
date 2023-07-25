from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):   
    # número que identifica a usuario y Unique : para que el valorno pueda repetirse
    category_name  = models.CharField(max_length=20, unique = True)
    # Descripcion del usuario 
    description = models.CharField(max_length=255, blank =True)
    #Slug : es concepto que se utiliza en web ecommerce esta destinado este campo a estar dentro de la parte final de la URL y representa a la entidad.
    slug = models.CharField(max_length=100, unique= True)
    #cat_image = Imagen que subirá el usuario 
    cat_image = models.ImageField(upload_to= 'photos/categories/' , blank = True)

# verbose_name el nombre en sigular category
# el nombre en plural categories todo esto para correguirlo en Django Admin
    class Meta:
       verbose_name = 'category'
       verbose_name_plural  = 'categories'
# EN CONCLUSION LO QUE HACE ESTE RETURN REVERSE ES CREADO GENERANDO UNA VARIABLE LOCALHOST:800/StORE  Y AGREGANDOLE EL SLUG 

# self : es el objeto categoria 
# Products by category es la ruta del archivo 
# reverse me va a devolver la url 
# products_by_category veine siendo el nombre de la ruta del slug

#En resumen, la función get_url devuelve la URL de una vista llamada 'products_by_category' con el argumento self.slug. Esto sugiere que la función se utiliza para generar una URL que muestra los productos asociados a una categoría específica en un sitio web o aplicación.

    def get_url(self):
        return reverse('products_by_category',args =[self.slug])


# Le dijo que retorne el valor  campo categoria en el DJANGO ADMIN 
    def __str__(self):
        return self.category_name