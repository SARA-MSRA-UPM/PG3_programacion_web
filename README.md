# Practica Guiada 3 - Programación Web

Este repositorio contiene el código de la práctica entregable "Tiempo Real" de
la asignatura Software Avanzado Radar (SARA) del Master en Sistemas Radar.

El repositorio contiene las siguientes carpetas:

- `app`: contiene el archivo main.py para ejecutar la aplicación y ficheros
relacionados con el código de la aplicación.
- `app/src`: contiene cada uno de los paquetes de python que usaremos durante el
  desarrollo de la práctica dividido de forma básica por las diferentes
  funcionalidades.
  - `actors`: contiene las distintas clases con la lógica de funcionamiento
  principal de la práctica
  - `helpers`: contiene archivos con funcionalidades generales del proyecto que
  pueden ser utilizada por cualquier clase principal.
  - `models`: contine clases que actuan como modelos de datos del proyecto.
  - `monitors`: contiene las clases relacionadas con la implementación de los
  monitores de la práctica.

## Escenario de la práctica

El escenario de la práctica consiste en una implementación de un modelo
digital de un radar. Además del modelo del radar también existe un modelo
digital de puntos con distintas características que pueden ser detectados por
el radar. La esctructura de la práctica es similar a la
[Práctica Guiada 1](https://github.com/SARA-MSRA-UPM/PG1_concurrencia), con la
diferencia de que la lógica de los radares está implementada en un servidor
externo.

Además necesitaremos para la ejecución de nuetra práctica un servidor local que
simula el escenario de radares. Este servidor está desarrollado en el proyecto
[RadarServer](https://github.com/SARA-MSRA-UPM/RadarServer). Para el desarrollar
la práctica es necesario arrancar el servidor de `RadarServer` como se describe
más adelante.

## Ejecución

### Arranque del servidor Radar Server

El primer paso para realizar esta práctica es descargar el proyecto
[RadarServer](https://github.com/SARA-MSRA-UPM/RadarServer) y arrancar el
servidor allí desarrollado tal y como se indica en sus instrucciones. Esto es
indispensable para el desarrollo de la práctica.

### Ejecución de la práctica

El primer paso para poder ejecutar la práctica y comprobar su funcionamiento
será la creación de un entorno virtual propio del proyecto. Normalmente el IDE
al no encontrar un entorno virtual creado preguntará automáticamente si se desea
crearlo. En cualquier caso se pude crear utilizando los siguientes comandos:

- Linux

```shell
python3 -m venv .venv
source .venv/bin/activate
```

- Windows

```powershell
python3 -m venv venv
venv\Scripts\Activate.ps1
```

Una vez creado el entorno virtual es necesario instalar las dependencias propias
del proyecto. Las dependencias están definidas en el fichero `requirements.txt`.
Generalmente hay opciones para instalarlas de forma automática desde el IDE,
pero también se pueden instalar manualmente utilizando el siguiente comando:

```shell
pip install -r requirements.txt
```

Por último tras instalar las dependencias necesarias en nuestro entorno virtual
podemos arrancar el proceso principal de nuestro proyecto ejecutando el fichero
`app/main.py`.

```shell
python3 app/main.py
```

## Objetivos a realizar

1. **Implementación de los modelos de datos** En todos los proyectos software
es importante crear los modelos de datos con los que trabajaremos. Estos modelos
representan los distintos elementos de nuestra lógica de negocio o de actuación.
Además la creación de estos modelos adquiere aún más relevancia cuando se trata
con integraciones con servicios de terceros, los cuales pueden no definir de la
misma forma que nosotros los modelos de datos.

- `RadarDetectionModel` representa las detecciones de los radares, por lo tanto,
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
intercambio de mensajes entre clientes y servidores es mediante una API REST. En
esta práctica realizaremos una integración con la API de `RadarServer` con el
objetivo de configurar el entorno adecuado para posteriormente obtener los datos
de las distintas detecciones.

3. **Integración con los sockets abiertos del RadarServer** La otra forma más
común para el intercambio de información en aplicaciones en red es la conexión a
sockets TCP del servidor. Como última parte de la práctica y habiendo realizado
la integración la API de `RadarServer` realizaremos una conexión mediante
sockets. Esta conexión nos servirá para obtener un stream de datos
correspondiente a las detecciones de los radares.
