Programa realizado siguiendo el tutorial de:
    https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/

Tips:
- Instalar python
- Crear un entorno
    python -m venv venv
- Activar entorno
- Instalar requerimientos
    pip install -r requeriments.txt

- para crear los modelos en la databases db
    python manage.py makemigrations
    python manage.py migrate

- crear superusuario
    python manage.py createsuperuser

- ejecutar servidor
    python manage.py runserver