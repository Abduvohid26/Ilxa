from django.contrib import admin

# Register your models here.
from products.models import Product, Category, Comment, Cart, ProductAuthor
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(ProductAuthor)