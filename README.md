***Blog de Autos - Guía de Prueba***

Este proyecto es un blog especializado en autos desarrollado con **Django**. A continuación, encontrarás una guía paso a paso para probar todas las funcionalidades.

**Configuración Inicial**

Inicia el servidor:

bashCopypython manage.py runserver

Visitá http://127.0.0.1:8000/

**Orden de Pruebas**

1. Gestión de Categorías
Primero, es necesario crear algunas categorías que usaremos más adelante:

Te dirigis a "Nueva Categoría" en la navegación
Creas al menos 3 categorías (ejemplo: Recomendado, No recomendado, Sin probar)
Podes ver todas las categorías creadas en "Ver Categorías"

2. Gestión de Autos
Una vez creadas las categorías, podes comenzar a agregar autos:

Vas a "Nuevo Auto"
Completa el formulario:

Marca y modelo
Año de fabricación
Descripción
Seleccioná una imagen
Asigná una o más categorías


Los autos creados aparecerán en la página principal

3. Gestión de Reseñas
Para cada auto se pueden agregar reseñas:

Vas a "Nueva Reseña"
Seleccioná el auto al que quieres agregar la reseña
Completa:

Título de la reseña
Contenido


Las reseñas quedarán vinculadas al auto seleccionado

4. Edición de Autos
Para cada auto creado podrás:

Modificar sus datos desde el botón "Editar"
Cambiar su imagen
Actualizar las categorías asignadas

5. Búsqueda
Proba el buscador en la parte superior:

Búsqueda por marca
Búsqueda por modelo

Ubicación de Funcionalidades
Templates
Ubicados en blog/templates/blog/:

base.html: Template principal con navegación
home.html: Página principal con lista de autos
auto_form.html: Formulario para crear/editar autos
categoria_form.html: Formulario de categorías
lista_categorias.html: Vista de categorías existentes

Vistas
En blog/views.py:

home: Vista principal
auto_nuevo: Creación de autos
auto_editar: Edición de autos existentes
categoria_nueva: Creación de categorías
lista_categorias: Visualización de categorías
buscar: Función de búsqueda

Modelos
En blog/models.py:

Auto: Información de vehículos
Categoria: Clasificación de autos

Notas Importantes

Las imágenes se guardan en la carpeta media/autos/
