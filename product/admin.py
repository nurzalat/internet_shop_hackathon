from django.contrib import admin
from product.models import Product, Category,Comment, Likes

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Likes)


