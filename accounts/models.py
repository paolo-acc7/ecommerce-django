from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager 
# Vamos a crear las clases que tenga las operaciones que me permitan crear un nuevo usuario y un nuevo superadmin usuario.
class MyAccountManager(BaseUserManager):
  # funcion crear usuario pasandole todos los valores que se detallan a countinucaion 
  def create_user(self, first_name, last_name, username, email, password = None):
      # Si el valor de E-mail es nullo entonces que dispare este error 
      if not email:
          raise ValueError('El usuario debe tener el email')
      # Y si no tiene un usuario que dispare este error 
      if not username:
          raise ValueError('El usuario debe tener el username')
      
      # si tiene email y username debe seguir en la siguiente linea 
      # esta es la instancia que se esta utilizando para crear un nuevo usuario 
      #Este código parece ser una parte de un método que se utiliza para crear y guardar un nuevo usuario en una base de datos. Veamos en detalle cada línea:
      #Aquí se está creando una nueva instancia de un modelo que probablemente representa a un usuario en una base de datos. Los parámetros de este modelo son pasados a través de un constructor. self.normalize_email(email) es probablemente una función que se encarga de validar y formatear la dirección de correo electrónico, y los otros parámetros son simplemente valores que se establecen para el usuario.
      user = self.model(
          email = self.normalize_email(email),
          username = username,
          first_name = first_name,
          last_name = last_name,
      )
#Aquí se establece la contraseña del usuario utilizando el método set_password(), que probablemente establece una versión hash de la contraseña para mejorar la seguridad. Se espera que password sea una cadena que contenga la contraseña del usuario.
      user.set_password(password)

#Finalmente, se guarda el objeto user en la base de datos utilizando el método save(). using=self._db es probablemente una especificación de la base de datos en la que se debe guardar el objeto.

#En general, este código parece ser una forma común de crear y guardar un usuario en una base de datos utilizando un modelo específico en Python. El método set_password() y la validación de correo electrónico ayudan a garantizar la seguridad y la integridad de la información del usuario.
      user.save(using = self._db)
      return user
#  esta funcion es para crear un superusurio
  def create_superuser(self, first_name, last_name, email, username, password):
#Aquí se está creando una nueva instancia de un modelo que probablemente representa a un usuario en una base de datos. Los parámetros de este modelo son pasados a través de un constructor. self.normalize_email(email) es probablemente una función que se encarga de validar y formatear la dirección de correo electrónico, y los otros parámetros son simplemente valores que se establecen para el usuario.
      user = self.create_user(
          email = self.normalize_email(email),
          username = username,
          password= password,
          first_name = first_name,
          last_name = last_name,
      )
# aqui les estamos cambiando los valores a los atributos para que sean verdaderos 
      user.is_admin = True
      user.is_active = True
      user.is_staff = True
      user.is_superadmin = True
#En general, este código parece ser una forma común de crear y guardar un usuario en una base de datos utilizando un modelo específico en Python. El método set_password() y la validación de correo electrónico ayudan a garantizar la seguridad y la integridad de la información del usuario.
      user.save(using = self._db)
      return user
    
# Create your models here.
class Account(AbstractBaseUser):
    #Campos personalizados para la clase Account
    # Primer Nombre 
    first_name = models.CharField(max_length=50)
    # Last name (Apellido)
    last_name = models.CharField(max_length=50)
    # nombre de usuario 
    username = models.CharField(max_length=50, unique=True)
    # correo electronico
    email = models.CharField(max_length=100, unique = True)
    # Número de telefono
    phone_number = models.CharField(max_length=50)

    # campos atributos de Django
    # Estos campos lo necesita Django por defecto por que de lo contrario
    # te presentara errores.
    # Fecha en la que se esta creando el  usuario
    date_joined = models.DateTimeField(auto_now_add=True)
    # utltima vez que el usuario inicio sesion
    last_login = models.DateTimeField(auto_now_add=True)
    # Es administrador este usuario 
    is_admin = models.BooleanField(default=False)
    # Este Usuario es parte del staff y le digo que por defecto el valor
    # sea falso
    is_staff = models.BooleanField(default=False)
    # Esta activo por defecto false 
    is_active = models.BooleanField(default=False)
    # Si es un super ADMIN  
    is_superadmin = models.BooleanField(default=False)

# el siguiente codigo es para que el usuario inicie sesion desde el E-mail 
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
# Aqui lo que estamos realizando es incluir los metodos de myaccountmanager en el modelo Account 

    objects = MyAccountManager()
#Este código es para listar los records de una entidad de una tabla yo quiero que se liste un label que represente cada récord 

    def __str__(self):
     return self.email

#Si tiene permisos para acceder  a labores de administrador solo va a retornalo si el atributo  is_admin devuelve commo true  
    def has_perm(self,perm,obj=None):
     return self.is_admin

# Le dan acesso a los modulos cuando es administrador
    def has_module_perms(self,add_label):
     return True


