Blog de Autos - Guía de Pruebas y Funcionalidades
Esta guía te ayudará a probar todas las funcionalidades del blog de autos en orden lógico.
Orden de Pruebas
1. Configuración Inicial
bashCopypython manage.py runserver
Visita http://127.0.0.1:8000/
2. Prueba de Funcionalidades (en este orden)
A. Creación de Categorías

Click en "Nueva Categoría" en la navegación
Completa el formulario:

Nombre (ejemplo: "Deportivos")
Descripción
Selecciona autos (estará vacío en este momento)



B. Creación de Autos

Click en "Nuevo Auto" en la navegación
Completa el formulario:

Marca (ejemplo: "Ferrari")
Modelo (ejemplo: "F40")
Año (ejemplo: "1987")
Descripción



C. Creación de Reseñas

Click en "Nueva Reseña" en la navegación
Completa el formulario:

Selecciona el auto creado anteriormente
Añade título
Escribe el contenido de la reseña



D. Búsqueda

Usa el buscador en la parte superior
Prueba buscar por:

Marca del auto creado
Modelo del auto creado



3. Ubicación de las Funcionalidades
Plantillas (templates/blog/)

base.html: Template principal con navegación
home.html: Página de inicio con lista de autos
auto_form.html: Formulario de creación de autos
reseña_form.html: Formulario de creación de reseñas
categoria_form.html: Formulario de creación de categorías
buscar.html: Resultados de búsqueda

Vistas (views.py)

home: Vista de la página principal
auto_nuevo: Creación de autos
reseña_nueva: Creación de reseñas
categoria_nueva: Creación de categorías
buscar: Función de búsqueda

Modelos (models.py)

Auto: Datos de los vehículos
Reseña: Reseñas de los autos
Categoria: Categorización de vehículos

URLs (urls.py)

/: Página principal
/auto/nuevo/: Crear auto
/reseña/nueva/: Crear reseña
/categoria/nueva/: Crear categoría
/buscar/: Búsqueda
