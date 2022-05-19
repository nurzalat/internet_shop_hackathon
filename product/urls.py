from django.urls import path, include
from product import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryView.as_view()),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())
]
