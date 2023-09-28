from django.db import models
from produtos.models.product import Product

class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    specification = models.TextField()

    def __str__(self):
        return f'Id Produto: {self.product.pk} | Especificação: {self.specification}'
    