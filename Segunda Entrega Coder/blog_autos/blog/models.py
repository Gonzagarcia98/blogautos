from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='autos/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"

class Reseña(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='reseñas')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    autos = models.ManyToManyField(Auto, related_name='categorias')
    
    def __str__(self):
        return self.nombre
