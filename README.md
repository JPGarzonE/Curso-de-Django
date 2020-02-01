# Curso de Django
Curso basico de Django en Platzi

## Preparación del entorno de trabajo

  - ### Instalación de python en windows
   1. Dirigirse a https://python.org
   2. Ir a la sección de descargas
   3. Descargar cualquier versión superior a 3.6.*
   
  - ### Instalación de python en linux
  ```
    $ dd-apt-repository -y ppa:jonathonf/python-3.6
    $ apt-get update -y
    $ apt-get install -y python3.6
    $ apt-get install -y python3.6-dev
    $ apt-get install -y python3.6-distutils
    $ ln -s /usr/bin/python3.6 /usr/local/bin/python3
    $ wget https://bootstrap.pypa.io/get-pip.py -O /home/ubuntu/get-pip.py
    $ python3.6 /home/ubuntu/get-pip.py
    $ rm /home/ubuntu/get-pip.py
    $ ln -s /usr/local/bin/pip /usr/local/bin/pip3
  ```
  
  - #### Verificación de la descarga
  ```
    $ python3 --version
  ```
  ```
    $ pip3 --version
  ```
  
  - #### Entorno virtual
  ```
    $ python3 -m venv ENTORNO
  ```
   Donde `ENTORNO` sea el nombre deseado
   
  ```
    $ source ENTORNO/bin/activate
  ```
   Para activar el entorno
   
  ```
    $ deactivate
  ```
   Para desactivar el entorno
  
  - #### Instalación de Django
  1. Activar entorno virtual y luego ejecutar:
  ```
    $ pip3 install django -U
    Ó
    $ pip install django -U
  ```

## Comandos necesarios para el desarrollo del proyecto

  - ### Para crear un proyecto de Django:
  ```
    $ django-admin startproject <nombre del proyecto> <ubicación del proyecto>
  ```
   Apenas se ejecuta el comando, se crea el proyecto en una carpeta del nombre y un archivo llamado manage.py que es clave (se encarga      de ejecutar los comandos de Django)
  
   Ej: Se crea un proyecto de django llamado platzigram en la carpeta actual
   ```
     $ django-admin startproject platzigram .
   ```

  - ### Para correr el servidor de Django:
  ```
    $ python3 manage.py runserver
  ```
  
  - ### Para crear una aplicación en el proyecto de Django:
  ```
    $ python3 manage.py startapp <nombre de la app>
  ```
  
  - ### Para ejecutar/realizar las migraciones necesarias:
  ```
    $ python3 manage.py migrate
  ```
  
  - ### Para que django rebice los cambios en las apps y cree las migraciones para ejecutarlas:
  ```
    $ python3 manage.py makemigrations
  ```
  
  - ### Para cargar el shell especial de Django:
  
  Util para hacer debugging y escribir codigo relacionado a django en la terminal
  ```
    $ python3 manage.py shell
  ```
 
## Registros en la base datos (Django):

### [Queries (acciones) que se pueden realizar a la BD en Django](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

Django cuenta con una interfaz que permite crear y traer datos llamada `objects`.

Se usa el modelo de datos y se llama a su atributo Objects: Ex `User.objects`.

  - ### Agregar registros a la Base de datos:
    - Hay dos formas de realizar esta acción:
      - A. usando .create():
    
      ```python
        from posts.model import User

        pablo = User.objects.create(
          email = '<email_de_pablo>',
          password = '<contraseña_de_pablo>',
          first_name = '<nombre_de_pablo>',
          last_name = '<apellido_de_pablo>',
          etc...
        )

        # Y ya queda registrado el usuario en la BD
      ```
      
      - B. Instanciando la clase a guardar:
      
      ```python
        from posts.model import User

        arturo = User()
        arturo.email = '<email_de_arturo>'
        password = '<contraseña_de_arturo>'
        first_name = '<nombre_de_arturo>'
        last_name = '<apellido_de_arturo>'
        etc...
        
        arturo.save() # Para guardar la instancia a la BD
      ```
      
  - ### Borrar un registro de la Base de datos:
  
    ```python
      from posts.model import User
      
      arturo.delete()
    ```
    
  - ### Obtener un usuario de la Base de datos:
    - Con un valor unico del usuario (Con el metodo get() solo se puede traer UN usuario)
    ```python
      from posts.model import User
      
      user = User.objects.get(email='<nombre_email>')
      
      user.email
      # --> <email_del_usuario>
      user.name
      # --> <nombre_del_usuario>
      user.last_name
      # --> <apellido_del_usuario>
    ```
    - Si el usuario al que se le hace el querie no existe envie un error:
    ```
      posts.models.DoesNotExist: User matching query does not exist.
    ```
  
  - ### Actualizar un registro de la Base de datos:
    - Tener al usuario en una variable, modificar el atributo que se desea y guardarlo en la BD
    ```python
      from posts.model import User
      
      user.email = '<nuevo_email>'
      
      user.save() # Se guarda de nuevo y listo
    ```
    
  - ### Obtener varios usuarios de la Base de datos:
    - Traer a todos los usuarios:
    ```python
      from posts.model import User
  
      users = User.objects.all() # devuelve un queryset con todos los usuarios
    ```
    
    - Con un filtro que devuelva los que cumplen con los criterios:
    ```python
      from posts.model import User
      
      platziUsers = User.objects.filter(email__endswith = '@platzi.com')
      # devuelve un queryset con los usuarios que tengan un correo que termine en '@platzi.com'
    ```
  
  - ### Actualizar varios registros de la Base de datos:
    ```python
      User.objects.filter(email__endswith = '@platzi.com').update(is_admin=True)
      # Esta haciendo admin a todos los usuarios con correo '@platzi.com'
    ```
    
## Glosario:

  - **ORM:** Object-relational mapping. Es el encargado de permitir el acceso y control de una base de datos relacional a través de una abstracción a clases y objetos.

  - **Templates:** Archivos HTML que permiten la inclusión y ejecución de lógica especial para la presentación de datos.

  - **Modelo:** Parte de un proyecto de Django que se encarga de estructurar las tablas y propiedades de la base de datos a través de clases de Python.

  - **Vista:** Parte de un proyecto de Django que se encarga de la lógica de negocio y es la conexión entre el template y el modelo.

  - **App:** Conjunto de código que se encarga de resolver una parte muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

  - **Patrón de diseño:** Solución común a un problema particular.
