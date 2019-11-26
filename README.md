# ws-functionalpython
App para aplicación de ejemplo en el workshop de python.


## Requisitos

Python 3.*

VS Code (preferentemente) o cualquier IDE de tu preferencia

### Pip

Tener actualizado pip:
***
$ python -m pip install --upgrade pip
***


Si tienes Mac Os, haslo despues de ejecutar:


```$ sudo su```


### Virtual Env

Instalar virtualenv (si tienes mac, ejecuta antes sudo su):

```$ pip install virtualenv```

Crear un ambiente virtual dentro del directorio de tu proyecto o carpeta raiz:

```$ cd directorio_raiz```

```$ virtualenv nombre_ambiente``` 

El param **nombre_ambiente** es el nombre de tu ambiente virtual, suele usarse el nombre **env**


#### Activar ambiente virtual:

```$ nombre_ambiente\Scripts\activate``` Windows

```$ source nombre_ambiente/bin/activate``` Mac Os o Linux


#### Desactivar ambiente virtual:

```$ nombre_ambiente\Scripts\deactivate``` Windows

```$ deactivate``` Mac Os o Linux


### Requests
[Requests es una libreria para python que nos permite ejecutar peticiones HTTP de una manera simple](https://requests.readthedocs.io/en/master/)

**Debes tener tu ambiente virtual activado**

Instalar requests:

```$ pip install requests```

