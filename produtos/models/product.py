from django.db import models
from produtos.models.mark import Mark
from produtos.models.model import Model
from produtos.models.typeWeight import TypeWeight
import decimal

class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='produtos/principal/', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1)
    creditCard = models.IntegerField()
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    guarantee = models.IntegerField()
    typeWeight = models.ForeignKey(TypeWeight, on_delete=models.PROTECT)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    
    def pixPrice(self):
        price = self.price * decimal.Decimal((100 - 15) / 100)
        return round(price, 2)
    
    def creditCardPrice(self):
        price = self.price / self.creditCard
        return round(price, 2)
    
    def __str__(self):
        return f'{self.pk} {self.name}'
