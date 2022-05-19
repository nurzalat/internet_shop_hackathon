from rest_framework import serializers
from product.models import Product, Category, Comment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # print('REPR',representation)
        representation['category'] = CategorySerializer(instance.category).data
        representation['comments_detail'] = CommentSerializer(instance.comments.all(), many=True).data
        return representation

    def create(self, validated_data):
        # request = self.context.get('request')
        created_product = Product.objects.create(**validated_data)
        return created_product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner', 'product',)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.owner.email
        return representation
    

