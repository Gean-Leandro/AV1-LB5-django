from django.contrib import admin
from produtos.models.content import Content
from produtos.models.image import Image
from produtos.models.mark import Mark
from produtos.models.model import Model
from produtos.models.product import Product
from produtos.models.rate import Rate
from produtos.models.specifications import Specification
from produtos.models.typeWeight import TypeWeight

admin.site.register(Content)
admin.site.register(Image)
admin.site.register(Mark)
admin.site.register(Model)
admin.site.register(Product)
admin.site.register(Rate)
admin.site.register(Specification)
admin.site.register(TypeWeight)
