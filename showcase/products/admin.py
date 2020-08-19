from django.contrib import admin
from products.models import Product, Images



def make_published(modeladmin, request, queryset):
    queryset.update(active=True)
make_published.short_description = "Active"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(active=False)
make_unpublished.short_description = "Deactive"

class ProductAdmin(admin.ModelAdmin):
    list_filter = (
        ('active', admin.BooleanFieldListFilter),
    )
    list_display = ('name', 'active', 'price', 'unit_price')
    actions = [make_published, make_unpublished]


admin.site.register(Product, ProductAdmin)
