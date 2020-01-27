# Curso de Django
Curso basico de Django en Platzi

## Preparación del entorno de trabajo

  - ### Instalación de python en windows
   1. Dirigirse a https://python.org
   2. Ir a la sección de descargas
   3. Descargar cualquier versión superior a 3.6.*
   
  - ### Instalación de python en linux
  ```
    dd-apt-repository -y ppa:jonathonf/python-3.6
    apt-get update -y
    apt-get install -y python3.6
    apt-get install -y python3.6-dev
    apt-get install -y python3.6-distutils
    ln -s /usr/bin/python3.6 /usr/local/bin/python3
    wget https://bootstrap.pypa.io/get-pip.py -O /home/ubuntu/get-pip.py
    python3.6 /home/ubuntu/get-pip.py
    rm /home/ubuntu/get-pip.py
    ln -s /usr/local/bin/pip /usr/local/bin/pip3
  ```
  
  - #### Verificación de la descarga
  ```
    python3 --version
  ```
  ```
    pip3 --version
  ```
  
  - #### Entorno virtual
  ```
    python3 -m venv ENTORNO
  ```
   Donde `ENTORNO` sea el nombre deseado
   
  ```
   source ENTORNO/bin/activate
  ```
   Para activar el entorno
   
  ```
    deactivate
  ```
   Para desactivar el entorno
  
  - #### Instalación de Django
  1. Activar entorno virtual y luego ejecutar:
  ```
    pip3 install django -U
    Ó
    pip install django -U
  ```
