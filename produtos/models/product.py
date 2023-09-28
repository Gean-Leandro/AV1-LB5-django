from django.db import models
from produtos.models.mark import Mark
from produtos.models.model import Model
from produtos.models.typeWeight import TypeWeight

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    creditCard = models.IntegerField()
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    guarantee = models.IntegerField()
    typeWeight = models.ForeignKey(TypeWeight, on_delete=models.PROTECT)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.pk} {self.name}'
