from rest_framework import serializers

from basket.models import Basket
from product.models import Product


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username'
    )

    class Meta:
        model = Basket
        fields = ('user', 'product', 'quantity',)

    def create(self, validated_data):
        print('validated_data: ', validated_data)
        # request = self.context.get('request')
        item = Basket.objects.filter(product=validated_data['product'], user=validated_data['user'])
        if not item:
            created_order = Basket.objects.create(**validated_data)
            return created_order
        else:
            raise serializers.ValidationError('Item already in cart!')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product = Product.objects.get(pk=representation['product'])
        representation['product'] = product.title
        user = self.context.get('request').user
        representation['user'] = str(user)
        return representation
