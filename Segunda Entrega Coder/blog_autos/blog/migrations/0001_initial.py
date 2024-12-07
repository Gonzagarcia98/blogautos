# Generated by Django 4.2.16 on 2024-12-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Auto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marca", models.CharField(max_length=100)),
                ("modelo", models.CharField(max_length=100)),
                ("año", models.IntegerField()),
                ("descripcion", models.TextField()),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="autos/"),
                ),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Reseña",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("contenido", models.TextField()),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
                (
                    "auto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reseñas",
                        to="blog.auto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="auto",
            name="categorias",
            field=models.ManyToManyField(
                blank=True, related_name="autos_categoria", to="blog.categoria"
            ),
        ),
    ]
