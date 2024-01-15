from django.utils import timezone
from datetime import timezone

from django.core.validators import MinValueValidator,MaxValueValidator
from django.db import models
from shared.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=250)
    def __str__(self):
        return f"Category name ->  {self.name}"

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    month_price = models.PositiveIntegerField(default=0, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    likes = models.IntegerField(default=0, null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)
    discount_title = models.TextField(null=True, blank=True)
    discount_start_time = models.DateTimeField(null=True, blank=True)
    discount_end_time = models.DateTimeField(null=True, blank=True)
    def is_discount_active(self):
        now = timezone.now()
        return self.discount_start_time <= now <= self.discount_end_time if self.discount_start_time and self.discount_end_time else False


    @property
    def new_price(self):
        if self.discount:
            discount_percentage = self.discount / 100
            new_price = self.price - (discount_percentage * self.price)
            return new_price


    def __str__(self):
        return f"{self.title} {self.price}"



class ProductAuthor(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} by {self.product.title}"





class Comment(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return f" comment-> {self.product.title} by {self.user}"





class Cart(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    def __str__(self):
        return f" cart-> {self.product.title} by {self.user} qty -> {str(self.quantity)}"