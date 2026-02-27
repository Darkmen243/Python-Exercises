import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField("Стоимость продукта", max_digits=10, decimal_places=3)
    stock = models.PositiveIntegerField(verbose_name="Количество на складе")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    pass

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Status(models.TextChoices):
        draft = 'draft'
        paid = 'paid'
        cancelled = 'cancelled'
    status = models.CharField(max_length=9, choices=Status,default=Status.draft)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"Order {self.order_id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def subtotal(self):
        return self.price_at_purchase * self.quantity
    
    def clean(self):
        if self.quantity<=0:
            raise ValidationError("Quantity must be greater than zero.")
        if self.pk is None and self.quantity>self.product.stock:
            raise ValidationError('Not enough stock available')
        
    def save(self,*args,**kwargs):
        is_new = self.pk is None
        self.full_clean()
        if is_new:
            self.price_at_purchase = self.product.price
            self.product.stock -=self.quantity
            self.product.save()
        super().save(*args,**kwargs)
    def __str__(self):
        return f"{self.product.name} x {self.quantity} "
    

