from django.db import models
from produtos.models.product import Product

class Content(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    content = models.TextField()

    def __str__(self):
        return f'Id Produto: {self.product.pk} | Conteudo: {self.content}'
    