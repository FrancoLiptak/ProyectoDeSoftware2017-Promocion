# Proyecto de Software
# Trabajo de Promoción 2017

## Presentación del documento

Este documento presenta un informe acerca del Trabajo de Promoción, el cual tuvo por objetivo aprender una tecnología que hasta el momento era desconocida por los integrantes del grupo, y también subir la nota obtenida en la cursada.

La estructura del documento será la siguiente:

- Presentación del documento.
- Acerca del grupo.
- Fundamentación sobre el framework elegido.
- Descripción de módulos desarrollados durante la cursada que pudieron ser usados en el trabajo de promoción.
- Mecanismo provisto para manejo de seguridad y routing.
- Mecanismo provisto para operaciones CRUD.
- Forma de manejar MVC: árbol de directorios.
- Materiales de referencia.

## Acerca del grupo

El grupo en la cursada obtuvo un 6 (seis) como nota final, y estuvo compuesto por:

- Franco Emanuel Liptak
- Gastón Gustavo Ríos.
- Santiago Maceri.

El grupo que decidió continuar con el trabajo de promoción estuvo compuesto por:

- Franco Emanuel Liptak.
- Gastón Gustavo Ríos.

## Fundamentación sobre el framework elegido

El trabajo fue desarrollado con Django, un framework de desarrollo web de código abierto que trabaja sobre el lenguaje de programación Python.

Ninguno de los integrantes del grupo había usado Django previamente, y este trabajo sirvió para obtener conocimientos.

El grupo eligió Django por varias razones:

- Es conocido por facilitar mucho el diseño de sistemas complejos. Enfatiza la reutilización y la capacidad de conexión de los componentes.
- Se basa en la filosofía DRY (Don’t Repeat Yourself).
- La comunidad de Django es muy grande. A la hora de desarrollar una determinada funcionalidad, es conveniente ver si no existe un paquete que provea dicha funcionalidad, la cual se podría usar en nuestro proyecto con poca o ninguna modificación. Un claro ejemplo de esto en nuestro trabajo fue el desarrollo de la aplicación para el bot de Telegram.
- Django tiene un panel de administración que permite hacer un CRUD de los distintos modelos, lo cual puede ser muy cómodo. - Esto fue usado en nuestro trabajo para la configuración inicial del sitio.
- Incluye un ORM, que mapea fácilmente objetos a tablas en la base de datos. Es compatible con MySQL, SQLite, DB2 y PostgreSQL, entre otros. En nuestro trabajo usamos PostgreSQL.
- Utiliza QuerySet (conjunto de consultas). En esencia, un QuerySet sería una lista de objetos de un modelo determinado. Permite leer datos de la base, filtrarlos y ordenarlos.
- La migración se vuelve bastante fácil. Basta con usar el comando “makemigrations” para crear las migraciones, y “migrate”.
- Hay mucha documentación disponible, y tutoriales en internet.
- Django REST framework es un conjunto de herramientas que permite la construcción de APIs. Fue utilizado para la API de turnos.
- Es un framework muy usado actualmente. En busca de crecimiento profesional por parte de los integrantes del grupo, pareció importante tener una experiencia con este framework, y por ende con Python.

## Descripción de módulos desarrollados durante la cursada que pudieron ser usados en el trabajo de promoción

Ningún módulo desarrollado durante la cursada pudo ser reutilizado en el trabajo de promoción. La razón es que durante la cursada trabajamos con PHP (en su versión 5.6) y durante el trabajo de promoción utilizamos un framework basado en Python.
Por ende, todas las funcionalidades tuvieron que ser escritas nuevamente. 

Sin embargo, ciertas ideas usadas durante la cursada (sobre cómo desarrollar funcionalidades) pudieron ser aplicados durante el trabajo de promoción. También pudo ser reutilizada la parte de JavaScript, específicamente los gráficos y DataTables.

## Mecanismo provisto para manejo de seguridad y routing

### Seguridad

Django está diseñado para proteger los sitios automáticamente de muchos errores de seguridad comunes.

Protege de las SQL Injections: La API de bases de datos de Django escapa automáticamente de todos los parámetros especiales SQL, de acuerdo al uso de comillas del servidor de base de datos que se esté usando (en nuestro caso PostgreSQL).

Protege de Cross-Site Scripting (XSS): escapa de todo el contenido que pudiera ser enviado por un usuario. Django lo hace automáticamente.

El framework ofrece facilidades para otros tipos de ataques, que si bien no hay sido utilizados debido a que no hay sido considerados necesarios, se los nombra:

- Cross-Site Request Forgery.
- Session Forging/Hijacking.
- Inyección de cabeceras de email.
- Directory Traversal.
- Exposición de mensajes de error.

URL Dispatcher

En la carpeta del proyecto, Django tiene un archivo llamado “urls.py”, el cual se encarga de resolver las direcciones y delegar al módulo que corresponda (dentro de la aplicación) resolver la solicitud pedida por el cliente.

Prácticamente cada aplicación de nuestro trabajo (a excepción del Bot), tiene su propio archivo de rutas.

Para entender mejor, servirá un ejemplo:

En nuestro archivo “urls.py” antes nombrado, tenemos la siguiente línea de código:

   ```python
   path('patient/', include ('apps.patient.urls', namespace="patient")),
   ```

Básicamente, lo que hacemos es delegar al archivo “urls.py” de la aplicación “Patient”, la tarea de resolver dicha dirección. El archivo “urls.py” de Patient contiene:

```python
app_name = 'patient'
urlpatterns = [
   path('index', login_required(PatientList.as_view()), name='patient_index'),
   path('create', login_required(PatientCreate.as_view()), name='patient_create'),
   path('update/<pk>/', login_required(PatientUpdate.as_view()), name='patient_update'),
   path('delete/<pk>/', login_required(PatientDelete.as_view()), name='patient_delete'),
   path('show/<pk>/', login_required(PatientShow.as_view()), name='patient_show'),
]
```

Es decir, el archivo “urls.py” de Patient se encarga de resolver todas las direcciones comenzadas con ‘patient/’.

Todas las aplicaciones del sistema siguen la misma forma de trabajo.

## Mecanismo provisto para operaciones CRUD

Para estas operaciones usamos Clases Basadas en Vistas (también conocidas como Class Based Views). Si bien no es la única alternativa que ofrece Django (por ejemplo, también ofrece Vistas Basadas en Funciones), es la que nos ha resultado más simple.

Las Vistas Basadas en Clases son útiles para mantener el código más legible y reutilizable. Tienen el objetivo de hacer el desarrollo del proyecto más fácil. 

Django nos provee de “vistas genéricas”, que básicamente son tareas comunes (como mostrar una lista de objetos, crear, borrar o editar).

Ejemplos de vistas genéricas que han sido usadas en el proyecto son: ListView, DetailView, UpdateView, CreateView y DeleteView. Las mismas han sido utilizadas, por ejemplo, en las aplicaciones Patient, User y Configuration.

Por supuesto, para llevar a cabo las funcionalidades descritas, también se usó el URL Dispatcher, Modelos y Templates, entre otras cosas.

## Forma de manejar MVC: árbol de directorios

Django usa un patrón de diseño conocido como Modelo-Vista-Template.

Para Django, la vista describe el dato que es presentado al usuario. No es necesariamente como se vé el dato, sino qué dato se muestra. Entonces, una «vista» es la función de callback en Python para una URL en particular, porque esta función de callback describe cuál dato es presentado.

El Template es el contenido visual que se le mostrará al usuario.

Para Django, el «controlador» está en el mismo framework: la maquinaria que envía una petición a la vista apropiada, de acuerdo a la configuración de URL de Django.

El árbol de directorios (de manera resumida) es:

```
├── apps
	├── appointment
	├── bot
	├── configuration
	├── health_control
	├── patient
	├── report
	├── users
├── hospital_env
├── proyecto_hospital
	├── settings.py
	├── urls.py
├── static
	├── css
	├── datatables
	├── fonts
	├── img
	├── js
	├── localizacion
├── manage.py
├── templates
 	├── 403.html
 	├── 503.html
 	├── base
 	├── configuration
 	├── health_control
 	├── index
 	├── patient
 	├── report
 	└── users
```

## Materiales de referencia

- Documentación de Django 2.0: https://docs.djangoproject.com/en/2.0/
- Django REST framework: http://www.django-rest-framework.org/
- Django-TelegramBot: https://django-telegrambot.readthedocs.io/en/latest/
- Explicación MVT de Django: https://docs.djangoproject.com/es/2.0/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names
- Libro de Django 1.0 (si bien es una versión anterior, ha sido útil): http://librosweb.es/libro/django_1_0/
- Django Bootstrap 4: http://django-bootstrap4.readthedocs.io/en/stable/
- Django maintenance mode: https://github.com/fabiocaccamo/django-maintenance-mode
