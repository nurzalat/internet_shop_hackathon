from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from basket import serializers
from basket.models import Basket
from basket.permissions import IsOwner


class BasketViewSet(ModelViewSet):
    class Meta:
        model = Basket
        fields = '__all__'
    queryset = Basket.objects.all()
    permission_classes = [IsOwner, ]
    serializer_class = serializers.BasketSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        # only authenticated user can create a post
        if self.action in ('create',):
            return [permissions.IsAuthenticated()]
        # only owner of post can update/delete post/s
        elif self.action in ('update', 'partial_update', 'destroy',):
            return [IsOwner()]
        # everyone can view posts
        else:
            return [permissions.AllowAny()]

    def destroy(self, request, *args, **kwargs):
        # instance = self.get_object()
        instance = Basket.objects.get(product=kwargs['pk'], user=request.user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def list(self, request, *args, **kwargs):
        user = request.user
        products = Basket.objects.filter(user=user)
        serializer = serializers.BasketSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

