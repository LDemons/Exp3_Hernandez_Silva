from django.db import models


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de categoria")


    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, max_length=8, verbose_name="id de producto")
    precio = models.IntegerField(max_length=10, blank=True, verbose_name="Precio")
    stock = models.IntegerField(max_length=5, blank=True, verbose_name="Stock")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    descripcion = models.CharField(max_length=30, blank=True, verbose_name="Nombre producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")


    def __str__(self):
        return self.descripcion