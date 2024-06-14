from django.contrib import admin

# Register your models here.
from .models import Product,Contact

admin.site.register(Product)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name', 'mobile_number', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('user_name', 'mobile_number', 'product__name')