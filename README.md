# Reto UCU I, Febrero 2021

## Orquestación de servicios para una solución de Bioinformática



## Para levantar la pagina:

#### Agregar un archivo ".env" a la altura de manage.py, y poner adentro HOST_LOGS=<IP del servidor de greylog\>
  
#### Correr pip -r requirements.txt

### Correr a la altura de manage.py en ese orden
####  py manage.py makemigrations
####  py manage.py migrate
####  py manage.py createsuperuser
####  py manage.py runserver


## Para usar celery
#### celery -A RetoI worker --loglevel=INFO (Activa el worker, que recibe y ejecuta la cola)
#### celery -A RetoI beat --loglevel=INFO (Activa un "sender" periodico)

