from django.contrib import admin
from .models import Item, Interior

# class ItemAdmin(admin.ModelAdmin):
#     list_display = (
#         'item_name',
#         'item_pic',
#         'item_size_width',
#         'item_size_height',
#         'price',
#         'details',
#     )

admin.site.register(Item)
admin.site.register(Interior)

# Register your models here.
