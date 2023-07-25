from .models import Account
from django.contrib import admin
# libreria 
from django.contrib.auth.admin import UserAdmin
# importo el modelo Accounts

# Register your models here.
#Resitro el modelo Account 


class AccountAdmin(UserAdmin):
    # Las propiedades que quiero que se muestren dentro de la tabla de usuarios 
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login','date_joined', 'is_active')
    # Propiedad Quiero cuando un usuario le de clic a una particular columna este me linke al detalle del usuario.
    list_display_link = ('email', 'first_name','last_name')
    # los campos de lectura osea no quiero que se pueda copiar esste dato 
    readonly_fields = ('last_login', 'date_joined')
    # quiero que se organize de tipo ascendente dependiento de la fecha en que se unio a mi aplicación.
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 
# voy a pasarle el account admin  al register Account
admin.site.register(Account,AccountAdmin)