#Importa la clase admin del módulo django.contrib.
from django.contrib import admin
#Importa el modelo Product desde el archivo models.py en el mismo directorio.
from .models import Product
# Register your models here.
#Se define la clase Product que hereda de admin.ModelAdmin, lo que indica que es una clase de administración personalizada para el modelo Product.
class ProductAdmin(admin.ModelAdmin):

#list_display es una propiedad de la clase Product que define los campos que se mostrarán en la lista de objetos Product en la interfaz de administración. En este caso, los campos incluidos son product_name, price, stock, category, modified_date y is_available.
    list_display = ('product_name','price','stock','category','modified_date','is_available')

    #prepopulated_fields es una propiedad de la clase Product que define los campos que se prellenarán automáticamente en la interfaz de administración. En este caso, se prellenará el campo slug basado en el valor del campo product_name.
    prepopulated_fields = {'slug':('product_name',)}
#admin.site.register(Product, ProductAdmin) registra el modelo Product en la interfaz de administración de Django. Esto permite que el modelo sea administrado y se muestre en la interfaz de administración. Se utiliza la clase ProductAdmin personalizada como la configuración adicional para la administración del modelo Product.
admin.site.register(Product, ProductAdmin)

    # En resumen, este código configura la interfaz de administración de Django para el modelo Product. Define qué campos se mostrarán en la lista de productos y cómo se prellenará automáticamente el campo slug. Luego, registra el modelo Product en la interfaz de administración utilizando la configuración personalizada proporcionada por la clase ProductAdmin.