from django.contrib import admin
from mptt import admin as  mptt_admin
from product import models


# Register your models here.

class CategoryAdmin(mptt_admin.DraggableMPTTAdmin):
    pass
    # list_display = ('category_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_count')
    search_fields = ('product_name',)
    filter_horizontal = ('categories',)

admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Characteristic)
admin.site.register(models.Product, ProductAdmin)

