# Practica Entregable 3 - Programación Web

Este repositorio contiene el código de la práctica guiada "Programación Web"
de la asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:
- `app`: contiene el archivo main.py para ejecutar la aplicación y la carpeta
  `src` donde se sitúan el resto de archivos.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante
  el desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `dataModels`: contiene clases con las distintas estructuras de datos que se 
  utilizaran

## Escenario de la práctica
El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. 

Este escenario de radares durante esta práctica se ejecutará en un servidor 
local al cual podemos realizar peticiones. Como abstracción podemos suponer que 
el escenario de nuestro servidor es el mismo que durante la 
[Práctica Guiada 2](https://github.com/SARA-MSRA-UPM/PG2_tiempo_real).

## Ejecución
El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. En PyCharm es
posible crear un entorno virtual mediante la interfaz gráfica. En caso
necesario los comandos son los siguientes.
```
# Linux
# Crear
python3 -m venv venv
# Activar
source venv/bin/activate
# Desactivar
deactivate

# Windows
# Crear
python3 -m venv venv
# Activar
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1
# Desactivar
deactivate
```

Una vez creado el entorno virtual es necesario instalar las dependencias
propias del proyecto. Las dependencias están definidas en el fichero
`requirements.txt`. En PyCharm se pueden instalar las dependencias mediante la
interfaz gráfica. En caso necesario los comandos son los siguientes.
```
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno
virtual podemos arrancar el proceso principal de nuestro proyecto ejecutando
el fichero `app/main.py`.
```
python3 app/main.py
```

## Objetivos a realizar
1. **Implementación de los modelos de datos** En todos los proyectos software 
es importante crear los modelos de datos con los que trabajaremos. Estos 
modelos representan los distintos elementos de nuestra lógica de negocio o de 
actuación. Además la creación de estos modelos adquiere aún más relevancia 
cuando se trata con integraciones con servicios de terceros, los cuales pueden 
no definir de la misma forma que nosotros los modelos de datos.
  - `DetectionModel` representa las detecciones de los radares, por lo tanto, 
  contendrá los datos necesarios para representar una detección como son: 
    - Identificador del radar que realiza la detección.
    - Distancia al centro del radar del punto detectado.
    - Orientación relativa del radar donde ha detectado el punto.
  - `RadarModel` representa las detecciones de los radares, por lo tanto,
    contendrá los datos necesarios para representar una detección como son:
    - Identificador del radar.
    - Posición del centro del radar.
    - Rango de detección del radar.
    - Orientación inicial del radar.
    - Angulo de detección del radar (incremento).

2. **Integración con la API del RadarServer** Uno de los principales métodos de 
intercambio de mensajes entre clientes y servidores es mediante una API REST.
En esta práctica realizaremos una integración con la API de `RadarServer` con 
el objetivo de configurar el entorno adecuado para posteriormente obtener los 
datos de las distintas detecciones.

3. **Integración con los sockets abiertos del RadarServer** La otra forma más 
común para el intercambio de información en aplicaciones en red es la conexión 
a sockets TCP del servidor. Como última parte de la práctica y habiendo 
realizado la integración la API de `RadarServer` realizaremos una conexión 
mediante sockets. Esta conexión nos servirá para obtener un stream de datos 
correspondiente a las detecciones de los radares.
