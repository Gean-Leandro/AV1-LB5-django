from django.db import models
from produtos.models.product import Product

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='produtos/', unique=True)

    def __str__(self):
        return f'Id produto: {self.product.pk} | Url da imagem: {self.image}'
    