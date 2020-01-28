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
 
