from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from products.models import Product, Category, Comment, Cart, ProductAuthor
from products.serializers import ProductSerializer, CategorySerializer, CommentSerializer, CartSerializer, PtAuthorSerializer



# Create your views here.


class ProductAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'


class ProductAuthorAPIView(ListCreateAPIView):
    serializer_class = PtAuthorSerializer
    queryset = ProductAuthor.objects.all()

class ProductAuthorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PtAuthorSerializer
    queryset = ProductAuthor.objects.all()




class CategoryAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CommentAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()





class CartAPIView(ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
