from django.db import models

# Create your models here.


class Product(models.Model):

    class Category(models.TextChoices):
        TECNOLOGIA = "Tecnologia"
        MODA = "Moda"
        VIDEOJUEGOS = "VideoJuegos"
        NA = "Sin Categoria"

    product_name = models.CharField(max_length=50)
    valor_unitario = models.IntegerField(null=False)
    #imagen_principal = models.ImageField(upload_to="productos", null=True, blank=True)
    categoria = models.CharField(max_length=25, choices=Category.choices, default=Category.NA)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.product_name
