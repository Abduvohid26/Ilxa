from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import LogoutAPIView, RegisterAPIView
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('logout', LogoutAPIView.as_view(), name='logout'),

]