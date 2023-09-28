from django.db import models
from produtos.models.mark import Mark

class Model(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Marca: {self.mark.name} | Modelo: {self.name}'
    