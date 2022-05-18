from django.urls import path, include
from basket import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', views.BasketViewSet, basename='Basket')

urlpatterns = [
    path('', include(router.urls)),
]
