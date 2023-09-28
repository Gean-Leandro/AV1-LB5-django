from django.db import models
from produtos.models.product import Product

class Rate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    rate = models.TextField()

    def __str__(self):
        return f'Id: {self.pk} | Usuário: {self.username} | Nome do produto: {self.product.name}'
    