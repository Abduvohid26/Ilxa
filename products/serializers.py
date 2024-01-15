from rest_framework import serializers

from .models import Product, ProductAuthor, Category, Comment, Cart




class PtAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAuthor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product
        products_author = ProductAuthor()
        category = CategorySerializer()
        comment = CommentSerializer()
        cart = CartSerializer()

