from django.urls import path
from .views import ProductAPIView, CartAPIView, CommentAPIView, CategoryAPIView, ProductAuthorAPIView, ProductDetailAPIView, ProductAuthorDetailAPIView, CartDetailAPIView, CategoryDetailAPIView, CommentDetailAPIView

urlpatterns = [
    path('product', ProductAPIView.as_view()),
    path('product/<slug:slug>/', ProductDetailAPIView.as_view()),
    path('catogories', CategoryAPIView.as_view()),
    path('catogories/<str:pk>', CategoryDetailAPIView.as_view()),
    path('cart', CartAPIView.as_view()),
    path('cart/<int:pk>', CartDetailAPIView.as_view()),
    path('comment', CommentAPIView.as_view()),
    path('comment/<int:pk>', CommentDetailAPIView.as_view()),
    path('productauthor', ProductAuthorAPIView.as_view()),
    path('productauthor/<int:pk>', ProductAuthorDetailAPIView.as_view())
]