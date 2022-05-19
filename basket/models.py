from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class Basket(models.Model):
    user = models.ForeignKey(User, related_name='basket_to_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='basket_to_product', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
