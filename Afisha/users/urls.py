from django.urls import path
from .views import AuthorizationAPIView, RegistrationAPIView

urlpatterns = [
    path('login/', AuthorizationAPIView.as_view(), name='login'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
]
