#Este es un fragmento de código Python para la aplicación web Django. El código utiliza el módulo django.contrib.admin para registrar un modelo llamado Category en la interfaz de administración de Django. El código importa el modelo Category desde el archivo models.py de la misma aplicación.
from django.contrib import admin
# importamos el modelo para poder registralo
from .models import Category
# Register your models here.
#El siguiente paso es crear una clase llamada CategoryAdmin que hereda de la clase admin.ModelAdmin. Esta clase se utiliza para personalizar la forma en que se muestra el modelo Category en la interfaz de administración.
class CategoryAdmin(admin.ModelAdmin):
    #La propiedad prepopulated_fields se utiliza para indicar que el campo slug se debe generar automáticamente a partir del campo category_name. Esto significa que cuando el usuario ingresa un valor en el campo category_name, Django generará automáticamente un valor para el campo slug en función de ese valor.
    
    prepopulated_fields = {'slug':('category_name',)}
#La propiedad list_display se utiliza para especificar qué campos del modelo Category se deben mostrar en la lista de categorías en la interfaz de administración. En este caso, se muestran los campos category_name y slug.

    list_display = ('category_name','slug')

#Finalmente, el código registra el modelo Category en la interfaz de administración de Django utilizando la clase CategoryAdmin que acabamos de definir. Esto permitirá a los administradores de la aplicación gestionar los registros del modelo Category a través de la interfaz de administración de Django.
# Aqui registraremos el modelo Category
admin.site.register(Category, CategoryAdmin)



