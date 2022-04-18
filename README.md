### Metrobus Location REST API v0.0.1
---

<p align="center"><b>Acerca de</b></p>  
API REST que utiliza los datos abiertos de CDMX para consulta de la posición y disponibilidad de las unidades de su sistema de microbús. Para recabar datos se sirve de utilizar las APIs públicas https://datos.cdmx.gob.mx/ y https://www.bigdatacloud.com/.  

- De la **API CDMX** se extrae el ID/label de unidad y su geolocalización por longitud y latitud. Su consumo para extraer las posiciones en tiempo real requiere de permiso del gobierno, es por ello que por el momento sólo podemos consultar mediante la misma un registro de posiciones anteriores.
- La **API BigDataCloud** nos permite determinar la alcaldía correspondiente a una latitud y longitud, sin embargo solo podemos consultar una posición por request. Normalmente su consumo demoraría minutos dada la cantidad de unidades del microbús, sin embargo mediante el uso de concurrencia fue posible reducir el tiempo de consulta a solo unos pocos segundos.

---

<p align="center"><b>Requerimientos de ejecución</b></p>  

- docker  
- docker-compose  
- Conexión a internet

---

<p align="center"><b>Instrucciones de ejecución</b></p>  

**Descargar y posicionarse en carpeta**  

```git clone https://github.com/8XA/metrobus_location-arkon.git```  
```cd metrobus_location-arkon```  
  
  
**Correr tests**  

```docker-compose run web python manage.py test``` 
  
  
**Levantar API**  

```docker-compose up```  

---

<p align="center"><b>Instrucciones de uso</b></p>  

Inicialmente la base de datos está vacía, por lo que ningún EndPoint de consulta retornará valor alguno. Para canalizar la información que necesitamos desde las **APIS CDMX** y **BigDataCloud** a través de pipelines a nuestra base de datos, basta llamar al EndPoint:  

```/location/fetch-data```  
* *demora unos segundos en completar la tarea.*  
  
La API implementa swagger y este muestra su interfaz en la URL inicial del servidor (http://localhost:8000/), donde puede apreciarse a detalle cómo se consumen sus EndPoints, listados a continuación:  

```/location/alcaldias-disponibles```  
```/location/ubicacion-de-unidad/{label}```  
```/location/unidades-disponibles```  
```/location/unidades-en-alcaldia/{alcaldia}```  

---

<p align="center"><b>Notas</b></p>  

- Las variables de entorno están configuradas dentro del archivo 'docker-compose.yml' con el objetivo de que la API pueda ser probada al instante, sin embargo para entorno de producción debe cambiar y proteger estas variables.  
- El diagrama de la API puede apreciarse en el archivo [diagrama_API.pdf](https://github.com/8XA/metrobus_location-arkon/blob/master/diagrama_API.pdf) o editarse en https://app.diagrams.net/ utilizando el archivo [diagrama_API.drawio](https://github.com/8XA/metrobus_location-arkon/blob/master/diagrama_API.drawio).  
- La función 'get_units_information' contenida en el archivo [microbuses_information.py](https://github.com/8XA/metrobus_location-arkon/blob/master/container_home/metrobus_project/location_app/microbuses_information.py) se encarga de recabar la información a grabar en la base de datos y formatearla. Se desarrolló modular, de manera que aunque es llamada mediante un EndPoint, puede también ser adaptada y ejecutada desde una aplicación CLI.  

