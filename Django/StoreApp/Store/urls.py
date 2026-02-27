from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from .views import *

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename='product')
router.register(r"orders",OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    ]
