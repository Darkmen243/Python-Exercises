from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField("Стоимость продукта", max_digits=10, decimal_places=3)
    stock = models.IntegerField(verbose_name="Количество на складе")
    is_active = models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
